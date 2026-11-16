"""
Núcleo comum do modelo de propagação de fake news.

Propósito:
    Reúne as constantes de estado e as funções compartilhadas por TODAS as
    versões do projeto (sequencial, paralela com threads, paralela com
    multiprocessing e distribuída com sockets).

Regra de ouro:
    Todas as versões DEVEM reutilizar `calcular_faixa` para calcular a próxima
    geração. Assim o comportamento lógico é idêntico em qualquer versão, e a
    equivalência (mesmas contagens por geração com a mesma semente) fica
    garantida por construção.

Relação com os outros arquivos:
    - sequencial.py: chama calcular_faixa sobre a grade inteira.
    - paralelo_threads.py / paralelo_mp.py: cada worker chama calcular_faixa
      sobre a sua faixa de linhas (intervalos vindos de particionar_linhas).
    - distribuido/trabalhador.py: chama calcular_faixa sobre a faixa local
      (com linhas de fronteira/halo recebidas dos vizinhos).
    - referencia/FakeNews_professor.py: implementação original, usada apenas
      como referência histórica (não deve ser editada).

Restrição: apenas biblioteca padrão (sem NumPy, Pandas, Numba, etc.).

Responsável: A definir
"""

# Estados possíveis de cada célula (pessoa) da grade.
IGNORANTE = 0   # ainda não recebeu/acredita na informação
ESPALHADOR = 1  # acredita e compartilha a informação
INATIVO = 2     # recebeu a informação, mas não compartilha mais


def criar_grade(linhas, colunas, percentual_espalhadores=0.02, semente=42):
    """
    Cria a grade inicial (lista de listas) com a maioria IGNORANTE e uma
    pequena fração ESPALHADOR sorteada com a semente informada.

    Parâmetros:
        linhas (int): número de linhas da grade.
        colunas (int): número de colunas da grade.
        percentual_espalhadores (float): fração inicial de espalhadores (0 a 1).
        semente (int): semente do gerador aleatório (reprodutibilidade).

    Retorno:
        list[list[int]]: grade linhas x colunas com os estados iniciais.

    Observação:
        Deve reproduzir EXATAMENTE o sorteio do professor (mesma sequência de
        random.randint) para que as contagens batam com a referência.
    """
    # TODO: implementar a partir de referencia/FakeNews_professor.py
    raise NotImplementedError


def contar_vizinhos_espalhadores(grade, i, j):
    """
    Conta os vizinhos ESPALHADOR da célula (i, j) na vizinhança de Moore
    (até 8 vizinhos; nas bordas há menos, pois a grade não é toroidal).

    Parâmetros:
        grade (list[list[int]]): grade lida (geração atual).
        i (int): linha da célula.
        j (int): coluna da célula.

    Retorno:
        int: quantidade de vizinhos no estado ESPALHADOR (0 a 8).
    """
    # TODO: implementar (atenção às bordas; na versão distribuída as linhas
    # de fronteira vêm do halo, então pense em como indexar a grade local).
    raise NotImplementedError


def calcular_faixa(grade_atual, grade_nova, linha_ini, linha_fim, limiar):
    """
    FUNÇÃO CENTRAL compartilhada por todas as versões.

    Calcula a próxima geração das linhas [linha_ini, linha_fim) lendo APENAS de
    `grade_atual` e escrevendo APENAS em `grade_nova`. Como cada faixa escreve
    em linhas disjuntas, várias threads/processos podem chamá-la ao mesmo tempo
    sem race condition.

    Regras aplicadas:
        - IGNORANTE vira ESPALHADOR se tiver >= `limiar` vizinhos ESPALHADOR.
        - ESPALHADOR vira INATIVO.
        - INATIVO permanece INATIVO.

    Parâmetros:
        grade_atual: grade da geração atual (somente leitura).
        grade_nova: grade da próxima geração (escrita apenas nas linhas da faixa).
        linha_ini (int): primeira linha da faixa (inclusive).
        linha_fim (int): última linha da faixa (exclusive).
        limiar (int): limiar de convencimento.

    Retorno:
        None (ou, opcionalmente, a contagem local de estados da faixa; decidir
        em grupo e documentar em docs/arquitetura.md).
    """
    # TODO: implementar sem deepcopy; usar contar_vizinhos_espalhadores.
    raise NotImplementedError


def contar_estados(grade, linha_ini=None, linha_fim=None):
    """
    Conta quantas células existem em cada estado, na grade inteira ou apenas
    nas linhas [linha_ini, linha_fim) (usado para contagem local por faixa).

    Parâmetros:
        grade: grade a ser contada.
        linha_ini (int | None): primeira linha (None = início da grade).
        linha_fim (int | None): linha final exclusiva (None = fim da grade).

    Retorno:
        dict[int, int]: {IGNORANTE: n0, ESPALHADOR: n1, INATIVO: n2}.
    """
    # TODO: implementar
    raise NotImplementedError


def particionar_linhas(total_linhas, n_partes):
    """
    Divide `total_linhas` em `n_partes` faixas contíguas e balanceadas.

    Parâmetros:
        total_linhas (int): número de linhas da grade.
        n_partes (int): número de faixas (threads/processos/trabalhadores).

    Retorno:
        list[tuple[int, int]]: lista de (linha_ini, linha_fim) por faixa, com
        fim exclusivo; as faixas cobrem todas as linhas, sem sobreposição.
        Definir o que acontece se n_partes > total_linhas.
    """
    # TODO: implementar (diferença de tamanho entre faixas <= 1 linha)
    raise NotImplementedError
