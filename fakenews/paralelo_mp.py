"""
Versão paralela com `multiprocessing` e memória compartilhada.

Propósito:
    Obter paralelismo REAL em Python (processos não compartilham o GIL).
    Complementa paralelo_threads.py, permitindo comparar as duas abordagens.

Estratégia (a implementar):
    - As duas grades (atual e nova) ficam em memória compartilhada, usando
      `multiprocessing.shared_memory.SharedMemory` ou `multiprocessing.Array`
      (grade achatada em 1D: índice = i * colunas + j). Decidir em grupo qual
      usar e documentar em docs/arquitetura.md.
    - Cada processo recebe uma faixa de linhas (modelo.particionar_linhas) e
      escreve só nela (faixas disjuntas => sem race condition na escrita).
    - `multiprocessing.Barrier` sincroniza os processos a cada geração.
    - Cada processo conta localmente os estados da sua faixa e grava a
      contagem num vetor compartilhado; a redução (soma) ocorre após a barreira.
    - Atenção: calcular_faixa foi escrita para listas de listas; adaptar o
      acesso à memória compartilhada SEM duplicar a regra do modelo
      (pense em como reaproveitar a mesma função).
    - Liberar a memória compartilhada (close/unlink) ao final.

Relação com os outros arquivos:
    - Usa fakenews/modelo.py; deve igualar sequencial.py nas contagens.

Responsável: A definir
"""

import multiprocessing  # noqa: F401  (será usado na implementação)

from fakenews import modelo  # noqa: F401


def executar_simulacao_paralela(
    linhas=100,
    colunas=100,
    geracoes=50,
    percentual_espalhadores=0.02,
    limiar_convencimento=2,
    n_workers=4,
    semente=42,
):
    """
    Executa a simulação com `n_workers` processos e memória compartilhada.

    Parâmetros: iguais aos da versão sequencial, mais `n_workers` (nº de processos).

    Retorno (mesmo formato da versão sequencial):
        (contagens_por_geracao, tempo_s).
    """
    # TODO: criar memória compartilhada, Barrier, processos; join; limpar.
    raise NotImplementedError


def trabalhador_processo(id_worker, linha_ini, linha_fim, parametros, barreira):
    """
    Função executada por cada processo (deve ser de nível de módulo para ser
    "picklável" no macOS/Windows, que usam o método de início 'spawn').

    Em cada geração: calcula a faixa, espera na barreira, conta localmente,
    grava a contagem no vetor compartilhado e espera na barreira para a
    redução e a troca das grades.

    Parâmetros:
        id_worker (int): índice do processo.
        linha_ini (int), linha_fim (int): faixa [ini, fim).
        parametros: dimensões, limiar, gerações e nomes/handles da memória
            compartilhada.
        barreira (multiprocessing.Barrier): sincronização entre gerações.
    """
    # TODO: implementar o laço por geração
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: argumentos (argparse): --linhas, --colunas, --geracoes, --percentual,
    #   --limiar, --semente, --workers
    # Dica: no macOS usar proteção `if __name__ == "__main__"` (spawn).
    pass
