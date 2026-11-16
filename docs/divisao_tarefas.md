# Divisão de tarefas

## Papéis

| Papel | Responsabilidade | Nome | Melhorias candidatas |
|-------|------------------|------|----------------------|
| **P1** | Núcleo (`modelo.py`), sequencial, testes (`tests/`) | | Otimização sem `deepcopy`; estatísticas extras |
| **P2** | Versão paralela (`paralelo_threads.py`, `paralelo_mp.py`) | | Probabilidade de convencimento; resistência |
| **P3** | Versão distribuída (`distribuido/`) | | Redução de comunicação com bitmask; influenciadores/bots |
| **P4** | Experimentos, visualização e relatório/apresentação | | Visualização (heatmap/GIF); estatísticas extras |

Cada melhoria vale até 0,5 ponto e precisa estar bem documentada (ver [extensoes/README.md](../extensoes/README.md)).

## Cronograma (7 dias)

| Dia | P1 | P2 | P3 | P4 |
|-----|----|----|----|----|
| **1** | Ler código do professor; implementar `modelo.py` e `sequencial.py` | Estudar Barrier/shared_memory | Estudar sockets/protocolo | Preparar ambiente, esqueleto dos benchmarks |
| **2** | Testes do modelo; validar equivalência com o professor | `paralelo_threads.py` | `protocolo.py` | `cenarios.py`, `rodar_experimentos.py` |
| **3** | Testes de equivalência | `paralelo_mp.py` | `coordenador.py` / `trabalhador.py` | `visualizar.py` |
| **4** | Revisão cruzada; ajustes | Testes paralelo vs. sequencial | Halo exchange funcionando | Primeiros experimentos |
| **5** | Extensões (P1) | Extensões (P2) | Extensões (P3) | Experimentos completos; `graficos.py` |
| **6** | Revisão final do código; documentar extensões | Idem | Idem | Preencher `ambiente_experimental.md`; tabelas e análise |
| **7** | Congelar código e compactar entrega | Ensaio da apresentação | Ensaio da apresentação | Finalizar PDF da apresentação |

_Ajustar o cronograma conforme a realidade do grupo. Marcar checkpoints de integração nos dias 3 e 5._
