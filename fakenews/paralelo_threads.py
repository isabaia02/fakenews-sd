"""
Versão paralela com `threading`.

Propósito:
    Cumpre o requisito literal "versão com threads" e permite demonstrar, nos
    experimentos, a limitação do GIL do CPython: como o cálculo é CPU-bound em
    Python puro, o ganho de desempenho esperado é pequeno ou nulo.

Estratégia (a implementar):
    - Duas grades alternadas: grade_atual (leitura) e grade_nova (escrita).
    - A grade é dividida em faixas de linhas (modelo.particionar_linhas).
    - Cada thread chama modelo.calcular_faixa na sua faixa. Como as faixas são
      DISJUNTAS na escrita, não há race condition e não são necessários locks
      para as células.
    - threading.Barrier sincroniza as threads ao fim de cada geração:
        1) todas terminam de escrever em grade_nova;
        2) (uma única thread) troca grade_atual <-> grade_nova;
        3) cada thread conta localmente os estados da sua faixa; as contagens
           locais são reduzidas (somadas) DEPOIS da barreira, sem lock na
           parte quente do cálculo.
    - Condição de parada (sem espalhadores) deve ser decidida de forma
      consistente por todas as threads (ex.: ação da Barrier).

Relação com os outros arquivos:
    - Usa fakenews/modelo.py. Deve produzir as mesmas contagens que
      sequencial.py (ver tests/test_equivalencia.py).
    - Comparada com paralelo_mp.py nos benchmarks.

Responsável: A definir
"""

import threading  # noqa: F401  (será usado na implementação)

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
    Executa a simulação com `n_workers` threads.

    Parâmetros: iguais aos da versão sequencial, mais `n_workers` (nº de threads).

    Retorno (mesmo formato da versão sequencial):
        (contagens_por_geracao, tempo_s).
    """
    # TODO: criar grades, faixas, Barrier, threads; juntar (join) e retornar.
    raise NotImplementedError


def trabalhador_thread(id_worker, linha_ini, linha_fim, estado_compartilhado):
    """
    Função executada por cada thread.

    Em cada geração: calcula a sua faixa com modelo.calcular_faixa, espera na
    barreira, conta localmente os estados da faixa, escreve a contagem local
    em um espaço próprio (posição id_worker) e espera de novo na barreira para
    a redução e a troca das grades.

    Parâmetros:
        id_worker (int): índice da thread (0 .. n_workers-1).
        linha_ini (int), linha_fim (int): faixa [ini, fim) deste worker.
        estado_compartilhado: objeto/estrutura com as grades, a Barrier, os
            vetores de contagem local e a flag de parada.
    """
    # TODO: implementar o laço por geração com Barrier
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: argumentos (argparse): --linhas, --colunas, --geracoes, --percentual,
    #   --limiar, --semente, --workers
    pass
