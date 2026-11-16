# Arquitetura

> Documento a completar conforme as decisões forem tomadas em grupo.

## 1. Visão geral

Todas as versões compartilham o núcleo `fakenews/modelo.py`, em especial `calcular_faixa(grade_atual, grade_nova, linha_ini, linha_fim, limiar)`, que garante o mesmo comportamento lógico.

```
            modelo.py (calcular_faixa, particionar_linhas, ...)
                 ^          ^            ^            ^
                 |          |            |            |
         sequencial   paralelo_threads  paralelo_mp  distribuido/
```

## 2. Versão sequencial

Duas grades alternadas (`grade_atual`, `grade_nova`), sem `deepcopy`; ao fim de cada geração troca-se a referência.

## 3. Versão paralela (threads e multiprocessing)

### 3.1 Grades e faixas disjuntas

```
grade_atual (somente leitura)        grade_nova (escrita)
+----------------------+             +----------------------+
| faixa 0  (worker 0)  |  ---------> | faixa 0  (worker 0)  |
+----------------------+             +----------------------+
| faixa 1  (worker 1)  |  ---------> | faixa 1  (worker 1)  |
+----------------------+             +----------------------+
| faixa 2  (worker 2)  |  ---------> | faixa 2  (worker 2)  |
+----------------------+             +----------------------+
```

- Todos leem de `grade_atual` (inclusive linhas de outras faixas, nas fronteiras).
- Cada worker escreve **apenas** na sua faixa de `grade_nova` => sem race condition.

### 3.2 Sincronização por geração

```
worker 0:  calcula faixa --\
worker 1:  calcula faixa ---+--> [ BARREIRA ] --> conta local --> [ BARREIRA ] --> troca grades
worker 2:  calcula faixa --/                       (redução)
```

- 1ª barreira: todos terminaram de escrever `grade_nova`.
- Contagem local por faixa, reduzida (somada) depois da barreira.
- Decisão de parada consistente para todos os workers.

### 3.3 Diferenças

- **threading**: memória compartilhada simples, mas limitada pelo GIL (esperamos pouco ou nenhum speedup; é um resultado a documentar).
- **multiprocessing**: paralelismo real; grades em `multiprocessing.shared_memory`/`Array`.

_A completar: escolha da estrutura compartilhada, formato da grade (lista de listas vs. vetor 1D), tratamento de n_workers > linhas._

## 4. Versão distribuída (sockets)

### 4.1 Topologia

```
                    +----------------+
                    |  Coordenador   |
                    +----------------+
                   /   |      |      \      MSG_INICIAR / MSG_CONTAGEM
                  /    |      |       \     MSG_CONTINUAR / MSG_FIM
        +--------+ +--------+ +--------+ +--------+
        | Trab 0 | | Trab 1 | | Trab 2 | | Trab 3 |
        +--------+ +--------+ +--------+ +--------+
             \_______/ \_______/ \_______/
              halo      halo      halo        MSG_FRONTEIRA
```

Todos os processos rodam na mesma máquina (localhost, TCP).

### 4.2 Halo exchange

Cada trabalhador mantém sua faixa + 1 linha fantasma acima e 1 abaixo:

```
Trabalhador k            linha fantasma (cópia da última linha de k-1)
+---------------------+
| faixa local         |
+---------------------+
                         linha fantasma (cópia da primeira linha de k+1)
```

A cada geração: trocar fronteiras -> calcular faixa -> enviar contagem -> aguardar `MSG_CONTINUAR`/`MSG_FIM`.

### 4.3 Protocolo de mensagens

| Tipo            | Direção                          | Conteúdo                             |
|-----------------|----------------------------------|--------------------------------------|
| `MSG_INICIAR`   | coordenador -> trabalhador       | faixa inicial, parâmetros            |
| `MSG_FRONTEIRA` | trabalhador <-> trabalhador      | linha de halo                        |
| `MSG_CONTAGEM`  | trabalhador -> coordenador       | contagem local da geração            |
| `MSG_CONTINUAR` | coordenador -> trabalhadores     | seguir para a próxima geração        |
| `MSG_FIM`       | coordenador -> trabalhadores     | encerrar                             |

Enquadramento: prefixo de tamanho (`struct`) + tipo + corpo.

_A completar: troca de fronteira direta entre trabalhadores vs. intermediada pelo coordenador, prevenção de deadlock, coleta da grade final (se necessária), tratamento de falhas._
