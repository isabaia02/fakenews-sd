# Propagação de Fake News em Sistemas Paralelos e Distribuídos

Trabalho final da disciplina de Sistemas Distribuídos (UTFPR).

Simulação da propagação de uma fake news em uma grade 2D de pessoas, com três
versões: **sequencial**, **paralela** (threads e multiprocessing) e
**distribuída** (sockets TCP, coordenador/trabalhadores, em uma única máquina).
O objetivo é comparar desempenho (speedup e eficiência) preservando exatamente
o comportamento lógico da versão sequencial.

> **Status:** estrutura inicial. A lógica ainda **não** foi implementada; os
> comandos abaixo estão marcados como "a implementar".

## Modelo (resumo)

- Estados: `0` Ignorante, `1` Espalhador, `2` Inativo.
- Vizinhança de Moore (até 8 vizinhos), em gerações discretas.
- Ignorante vira Espalhador se tiver ao menos `limiar_convencimento` vizinhos Espalhadores; Espalhador vira Inativo na geração seguinte; Inativo permanece Inativo.
- Para quando não há mais espalhadores ou as gerações acabam.

Detalhes em [docs/modelo_computacional.md](docs/modelo_computacional.md).

## Estrutura de pastas

```
fakenews-sd/
├── README.md
├── CONTRIBUTING.md
├── requirements.txt
├── referencia/FakeNews_professor.py   # código do professor (intacto)
├── fakenews/
│   ├── modelo.py                      # constantes e funções compartilhadas
│   ├── sequencial.py
│   ├── paralelo_threads.py
│   ├── paralelo_mp.py
│   └── distribuido/
│       ├── protocolo.py
│       ├── coordenador.py
│       └── trabalhador.py
├── extensoes/                         # melhorias (ver extensoes/README.md)
├── visualizacao/visualizar.py
├── tests/
├── benchmarks/                        # experimentos e gráficos
└── docs/
```

## Pré-requisitos

- Python 3.10+ (desenvolvido com Python 3).
- As versões avaliadas usam **apenas a biblioteca padrão** (sem NumPy, Pandas, Numba, Cython ou GPU).
- `matplotlib` apenas para gráficos e visualização.

## Instalação

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # só necessário para gráficos/visualização
```

## Como executar (a implementar)

Execute sempre a partir da raiz do repositório.

```bash
# Sequencial (a implementar)
python -m fakenews.sequencial --linhas 100 --colunas 100 --geracoes 50

# Paralela com threads (a implementar)
python -m fakenews.paralelo_threads --workers 4

# Paralela com multiprocessing (a implementar)
python -m fakenews.paralelo_mp --workers 4

# Distribuída, em terminais separados (a implementar)
python -m fakenews.distribuido.coordenador --trabalhadores 4 --porta 5000
python -m fakenews.distribuido.trabalhador --porta 5000   # um por trabalhador

# Experimentos e gráficos (a implementar)
python -m benchmarks.rodar_experimentos --saida benchmarks/resultados/resultados.csv
python -m benchmarks.graficos --csv benchmarks/resultados/resultados.csv

# Visualização (a implementar)
python -m visualizacao.visualizar --saida propagacao.gif
```

## Testes

```bash
python -m unittest discover tests
```

Os testes estão como esqueleto (são ignorados até serem implementados).

## Integrantes

| Nome | Papel |
|------|-------|
|      | P1 — Núcleo, sequencial e testes |
|      | P2 — Versão paralela |
|      | P3 — Versão distribuída |
|      | P4 — Experimentos, visualização e relatório |

## Documentação

- [Arquitetura](docs/arquitetura.md)
- [Modelo computacional](docs/modelo_computacional.md)
- [Ambiente experimental](docs/ambiente_experimental.md)
- [Divisão de tarefas e cronograma](docs/divisao_tarefas.md)
- [Referências e uso de IA](docs/referencias.md)
- [Extensões](extensoes/README.md)
- [Como contribuir](CONTRIBUTING.md)

## Uso de IA generativa

Conforme exigido pelo professor, declaramos que ferramentas de IA generativa
foram usadas como **apoio** (por exemplo, na criação da estrutura inicial do
repositório e da documentação-base). O registro detalhado do que foi usado e
como está em [docs/referencias.md](docs/referencias.md). Todo o código
commitado deve ser compreendido pelo integrante que o submeteu.
