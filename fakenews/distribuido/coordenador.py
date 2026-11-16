"""
Coordenador da versão distribuída (arquitetura coordenador/trabalhadores).

Propósito:
    Inicia o servidor TCP, aceita N trabalhadores, distribui as faixas
    iniciais da grade, coleta as contagens por geração e decide se a simulação
    continua ou para (sem espalhadores ou gerações esgotadas).

Execução prevista:
    Tudo em UMA máquina (vários processos em localhost). Cada trabalhador é um
    processo separado que se conecta ao coordenador.

Fluxo (a implementar):
    1. Criar a grade inicial (modelo.criar_grade) e as faixas
       (modelo.particionar_linhas).
    2. Abrir o socket servidor e aceitar `n_trabalhadores` conexões.
    3. Enviar MSG_INICIAR a cada trabalhador com a sua faixa e parâmetros
       (e informações para localizar os vizinhos, se a troca de fronteira for
       direta entre trabalhadores).
    4. A cada geração: receber MSG_CONTAGEM de todos, somar, registrar e
       enviar MSG_CONTINUAR ou MSG_FIM.
    5. Fechar conexões e devolver as contagens por geração e o tempo.

Relação com os outros arquivos:
    - Usa protocolo.py e modelo.py; conversa com trabalhador.py.
    - Deve igualar sequencial.py nas contagens (tests/test_equivalencia.py).

Responsável: A definir
"""

import socket  # noqa: F401  (será usado na implementação)

from fakenews import modelo  # noqa: F401
from fakenews.distribuido import protocolo  # noqa: F401


def executar_coordenador(
    host="127.0.0.1",
    porta=5000,
    n_trabalhadores=4,
    linhas=100,
    colunas=100,
    geracoes=50,
    percentual_espalhadores=0.02,
    limiar_convencimento=2,
    semente=42,
):
    """
    Executa o coordenador até o fim da simulação.

    Parâmetros:
        host (str), porta (int): endereço onde o servidor escuta.
        n_trabalhadores (int): quantos trabalhadores esperar.
        demais: iguais aos da versão sequencial.

    Retorno:
        (contagens_por_geracao, tempo_s), no mesmo formato das outras versões.
    """
    # TODO: implementar o fluxo descrito no docstring do módulo
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: argumentos (argparse): --host, --porta, --trabalhadores, --linhas,
    #   --colunas, --geracoes, --percentual, --limiar, --semente
    pass
