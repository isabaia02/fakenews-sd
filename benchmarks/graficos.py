"""
Cálculo de speedup/eficiência e geração de tabelas e gráficos.

Propósito:
    Ler o CSV de rodar_experimentos.py e produzir:
      - Speedup:    S = Tseq / Tp
      - Eficiência: E = S / p   (p = nº de threads/processos/trabalhadores)
      - Tabelas (ex.: Markdown/CSV) e gráficos (matplotlib) para o relatório.

Relação com os outros arquivos:
    - Entrada: benchmarks/resultados/*.csv.
    - Usa matplotlib (requirements.txt); fora das versões avaliadas.

Responsável: A definir
"""


def carregar_resultados(caminho_csv):
    """
    Lê o CSV de resultados.

    Retorno:
        list[dict]: uma linha por execução.
    """
    # TODO: implementar com o módulo csv
    raise NotImplementedError


def calcular_tempo_medio(resultados, versao, **filtros):
    """
    Calcula o tempo médio (e desvio) de uma versão para um cenário.

    Parâmetros:
        resultados: linhas do CSV.
        versao (str): versão desejada.
        **filtros: valores de linhas, colunas, geracoes, n_workers, etc.

    Retorno:
        tuple[float, float]: (média, desvio padrão) de tempo_s.
    """
    # TODO: implementar (statistics da biblioteca padrão)
    raise NotImplementedError


def calcular_speedup(tempo_sequencial, tempo_paralelo):
    """
    Speedup S = Tseq / Tp.

    Retorno:
        float.
    """
    # TODO: implementar
    raise NotImplementedError


def calcular_eficiencia(speedup, n_workers):
    """
    Eficiência E = S / p.

    Retorno:
        float.
    """
    # TODO: implementar
    raise NotImplementedError


def gerar_tabela(resultados, caminho_saida):
    """
    Gera a tabela de tempos, speedup e eficiência por versão e nº de workers.

    Retorno:
        None (grava arquivo).
    """
    # TODO: implementar
    raise NotImplementedError


def gerar_grafico_speedup(resultados, caminho_saida):
    """
    Gráfico de speedup x nº de workers (com a linha ideal S = p).

    Retorno:
        None (grava imagem).
    """
    # TODO: implementar com matplotlib
    raise NotImplementedError


def gerar_grafico_eficiencia(resultados, caminho_saida):
    """
    Gráfico de eficiência x nº de workers.

    Retorno:
        None (grava imagem).
    """
    # TODO: implementar com matplotlib
    raise NotImplementedError


def gerar_grafico_tempo_vs_tamanho(resultados, caminho_saida):
    """
    Gráfico de tempo x tamanho da matriz, por versão.

    Retorno:
        None (grava imagem).
    """
    # TODO: implementar com matplotlib
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: argumentos (argparse): --csv, --saida
    pass
