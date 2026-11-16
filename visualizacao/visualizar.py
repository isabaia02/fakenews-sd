"""
Visualização da propagação de fake news (heatmap e GIF).

Propósito:
    Gerar imagens de uma geração (heatmap) e uma animação (GIF) da propagação,
    para a apresentação. Usa matplotlib (dependência externa permitida apenas
    para análise e visualização; NÃO deve ser importado pelas versões avaliadas).

Relação com os outros arquivos:
    - Consome grades produzidas por fakenews/sequencial.py (ou guardadas por
      geração). Pode exigir que a simulação exponha/salve a grade de cada
      geração (cuidado com memória em grades grandes; usar grades pequenas).

Responsável: A definir
"""


def gerar_heatmap(grade, geracao, caminho_saida):
    """
    Gera uma imagem (heatmap) de uma geração.

    Parâmetros:
        grade (list[list[int]]): grade a desenhar.
        geracao (int): número da geração (para o título).
        caminho_saida (str): arquivo PNG de saída.

    Retorno:
        None.
    """
    # TODO: implementar com matplotlib (cores distintas por estado + legenda)
    raise NotImplementedError


def gerar_gif(grades_por_geracao, caminho_saida, intervalo_ms=200):
    """
    Gera um GIF animado da propagação.

    Parâmetros:
        grades_por_geracao (list): grades de cada geração, em ordem.
        caminho_saida (str): arquivo GIF de saída.
        intervalo_ms (int): tempo entre quadros.

    Retorno:
        None.
    """
    # TODO: implementar (matplotlib.animation ou salvar quadros)
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: argumentos (argparse): --linhas, --colunas, --geracoes,
    #   --percentual, --limiar, --semente, --saida, --formato (png|gif)
    pass
