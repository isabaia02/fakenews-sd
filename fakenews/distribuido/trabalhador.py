"""
Trabalhador da versão distribuída.

Propósito:
    Conecta-se ao coordenador, recebe uma faixa de linhas da grade e, a cada
    geração, troca as linhas de fronteira com os vizinhos (halo exchange /
    ghost rows), calcula a faixa local e reporta as contagens ao coordenador.

Halo exchange (a implementar):
    - Cada trabalhador guarda a sua faixa mais 1 linha "fantasma" acima e 1
      abaixo (cópias das linhas de fronteira dos vizinhos).
    - A cada geração, antes de calcular: envia a sua primeira linha ao vizinho
      de cima e a última ao vizinho de baixo, e recebe as deles (MSG_FRONTEIRA).
    - Atenção ao DEADLOCK: se todos enviam e depois recebem com buffers
      pequenos, podem travar. Defina uma ordem (ex.: trabalhadores pares
      enviam primeiro, ímpares recebem primeiro) ou use threads/não bloqueante.
    - O primeiro e o último trabalhador não têm vizinho em uma das pontas
      (a grade não é toroidal): tratar como borda (linhas fora = sem vizinhos).
    - Calcular a faixa reutilizando modelo.calcular_faixa.

Relação com os outros arquivos:
    - Usa protocolo.py e modelo.py; conversa com coordenador.py.

Responsável: A definir
"""

import socket  # noqa: F401  (será usado na implementação)

from fakenews import modelo  # noqa: F401
from fakenews.distribuido import protocolo  # noqa: F401


def executar_trabalhador(host="127.0.0.1", porta=5000):
    """
    Executa um trabalhador até receber MSG_FIM.

    Parâmetros:
        host (str), porta (int): endereço do coordenador.

    Retorno:
        None.
    """
    # TODO: conectar, receber MSG_INICIAR, laço por geração, encerrar
    raise NotImplementedError


def trocar_fronteiras(faixa_local, sock_acima, sock_abaixo):
    """
    Troca as linhas de fronteira com os vizinhos (halo exchange).

    Parâmetros:
        faixa_local: linhas da faixa deste trabalhador.
        sock_acima, sock_abaixo: conexões com os vizinhos (None se não houver).

    Retorno:
        tuple: (linha_fantasma_acima, linha_fantasma_abaixo), com None onde
        não há vizinho.
    """
    # TODO: implementar evitando deadlock (ver docstring do módulo)
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: argumentos (argparse): --host, --porta
    pass
