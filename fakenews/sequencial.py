"""
Versão sequencial (refatorada) da simulação de propagação de fake news.

Propósito:
    Base de comparação (Tseq) para o cálculo de speedup e eficiência, e
    referência de corretude para as versões paralela e distribuída.

Relação com os outros arquivos:
    - Parte de referencia/FakeNews_professor.py (que NÃO deve ser editado).
    - Usa fakenews/modelo.py (constantes e `calcular_faixa`).
    - É usada por tests/test_equivalencia.py e benchmarks/rodar_experimentos.py.

Refatoração prevista (TODO):
    - Evitar `deepcopy` a cada geração: usar DUAS matrizes alternadas
      (grade_atual / grade_nova) e trocar as referências ao fim de cada geração.
    - Reutilizar `modelo.calcular_faixa` sobre a grade inteira
      (linha_ini=0, linha_fim=linhas), igual às demais versões.
    - Separar cálculo de impressão, para que o tempo medido não inclua I/O.
    - Devolver as contagens por geração (para os testes de equivalência).

Responsável: A definir
"""

from fakenews import modelo  # noqa: F401  (será usado na implementação)


def executar_simulacao(
    linhas=100,
    colunas=100,
    geracoes=50,
    percentual_espalhadores=0.02,
    limiar_convencimento=2,
    mostrar_grade=False,
    semente=42,
):
    """
    Executa a simulação sequencial completa.

    Parâmetros (mesmos da versão do professor, mais `semente`):
        linhas (int): linhas da grade.
        colunas (int): colunas da grade.
        geracoes (int): número máximo de gerações.
        percentual_espalhadores (float): fração inicial de espalhadores.
        limiar_convencimento (int): vizinhos espalhadores necessários.
        mostrar_grade (bool): imprime a grade a cada geração (só p/ grades pequenas).
        semente (int): semente do sorteio inicial.

    Retorno (a definir em grupo):
        Sugestão: (contagens_por_geracao, tempo_s), onde contagens_por_geracao
        é uma lista de dicts {IGNORANTE: n, ESPALHADOR: n, INATIVO: n}.

    Para a execução:
        Para quando não há mais espalhadores ou quando as gerações acabam.
    """
    # TODO: refatorar a partir de referencia/FakeNews_professor.py
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: argumentos de linha de comando esperados (argparse):
    #   --linhas, --colunas, --geracoes, --percentual, --limiar, --semente,
    #   --mostrar-grade
    pass
