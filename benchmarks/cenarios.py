"""
Definição dos cenários dos experimentos.

Propósito:
    Centralizar quais combinações de parâmetros serão varridas por
    rodar_experimentos.py.

Variáveis a varrer (TODO: definir os valores concretos em grupo):
    - Tamanho da matriz (ex.: 100x100, 500x500, 1000x1000, ...).
    - Número de gerações (ex.: 50, 100, 200).
    - Percentual inicial de espalhadores (ex.: 0.01, 0.02, 0.05, 0.10).
    - Número de threads (ex.: 1, 2, 4, 8).
    - Número de processos (multiprocessing) e de trabalhadores (distribuído).
    - Limiar de convencimento (fixo ou variado).
    - Repetições por cenário (ex.: 3 a 5) para tirar média/desvio.

Regra: variar UMA variável por vez, mantendo as demais fixas (cenário-base),
para a análise ficar clara.

Relação com os outros arquivos:
    - Consumido por rodar_experimentos.py.

Responsável: A definir
"""


def obter_cenarios():
    """
    Devolve a lista de cenários a executar.

    Retorno:
        list[dict]: cada dict com as chaves linhas, colunas, geracoes,
        percentual_espalhadores, limiar, n_workers, repeticoes.
    """
    # TODO: implementar (gerar a lista a partir das variáveis acima)
    raise NotImplementedError
