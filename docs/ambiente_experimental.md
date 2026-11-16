# Ambiente experimental

Preencher com os dados da máquina onde os experimentos finais foram executados (e repetir por máquina, se houver mais de uma).

| Campo | Valor |
|-------|-------|
| Processador (modelo) | _a preencher_ |
| Núcleos físicos | _a preencher_ |
| Núcleos lógicos (threads de hardware) | _a preencher_ |
| Memória RAM | _a preencher_ |
| Sistema operacional (e versão) | _a preencher_ |
| Versão do Python (`python --version`) | _a preencher_ |
| Implementação do Python (CPython?) | _a preencher_ |
| Ambiente de execução (terminal, venv, Docker...) | _a preencher_ |
| Método de início do multiprocessing (`fork`/`spawn`) | _a preencher_ |
| Condições (máquina ociosa? na tomada? outros programas abertos?) | _a preencher_ |

## Como coletar

```bash
python --version
sysctl -n machdep.cpu.brand_string hw.physicalcpu hw.logicalcpu hw.memsize   # macOS
lscpu && free -h                                                              # Linux
```
