"""
Execução dos experimentos e gravação dos resultados em CSV.

Propósito:
    Varre os cenários (benchmarks/cenarios.py), executa cada versão (sequencial,
    threads, multiprocessing, distribuído) com repetições e grava o tempo.

Formato do CSV de saída (benchmarks/resultados/*.csv), uma linha por execução:
    versao, linhas, colunas, geracoes, percentual_espalhadores, limiar,
    n_workers, repeticao, tempo_s

    - versao: "sequencial" | "threads" | "multiprocessing" | "distribuido"
    - n_workers: 1 para a versão sequencial.
    - tempo_s: tempo de parede (time.perf_counter) só da simulação, sem
      impressão nem criação de processos/conexões (decidir em grupo se o custo
      de setup entra ou não, e documentar).

Boas práticas (TODO): descartar uma execução de aquecimento, manter a máquina
ociosa, registrar o ambiente em docs/ambiente_experimental.md.

Relação com os outros arquivos:
    - Usa cenarios.py e as versões em fakenews/.
    - Alimenta graficos.py.

Responsável: A definir
"""


def executar_cenario(versao, cenario, repeticao):
    """
    Executa uma versão em um cenário e mede o tempo.

    Parâmetros:
        versao (str): nome da versão.
        cenario (dict): parâmetros do cenário.
        repeticao (int): índice da repetição.

    Retorno:
        dict: uma linha do CSV (colunas descritas no docstring do módulo).
    """
    # TODO: implementar
    raise NotImplementedError


def rodar_todos(caminho_csv):
    """
    Executa todos os cenários e grava o CSV.

    Parâmetros:
        caminho_csv (str): arquivo de saída (em benchmarks/resultados/).

    Retorno:
        None.
    """
    # TODO: implementar (csv da biblioteca padrão; gravar incrementalmente
    # para não perder dados se a execução for interrompida)
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: argumentos (argparse): --saida, --versoes, --repeticoes, --rapido
    pass
