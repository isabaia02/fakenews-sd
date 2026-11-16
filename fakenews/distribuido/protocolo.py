"""
Protocolo de mensagens da versão distribuída (TCP / sockets).

Propósito:
    Define o formato das mensagens trocadas entre coordenador e trabalhadores
    e entre trabalhadores vizinhos (troca de linhas de fronteira).

Formato proposto (a confirmar em grupo; documentar em docs/arquitetura.md):
    [4 bytes: tamanho do corpo, big-endian (struct '!I')] [1 byte: tipo] [corpo]
    O prefixo de tamanho resolve o problema de TCP ser um fluxo de bytes (sem
    fronteiras de mensagem): é preciso ler EXATAMENTE `tamanho` bytes (laço
    sobre recv até completar).

Tipos de mensagem:
    MSG_INICIAR   coordenador -> trabalhador: faixa inicial e parâmetros.
    MSG_FRONTEIRA trabalhador <-> trabalhador (ou via coordenador): linha de halo.
    MSG_CONTAGEM  trabalhador -> coordenador: contagem local por geração.
    MSG_CONTINUAR coordenador -> trabalhadores: seguir para a próxima geração.
    MSG_FIM       coordenador -> trabalhadores: encerrar (e, se necessário,
                  trabalhador -> coordenador: devolver a faixa final).

Relação com os outros arquivos:
    - Usado por coordenador.py e trabalhador.py.
    - Serialização de linhas: usar apenas struct/bytes (sem pickle de objetos
      desconhecidos, por segurança). Ideia de extensão: empacotar 2 bits por
      célula (bitmask) para reduzir a comunicação.

Responsável: A definir
"""

import struct  # noqa: F401  (será usado na implementação)

# Tipos de mensagem (valores sugeridos).
MSG_INICIAR = 1
MSG_FRONTEIRA = 2
MSG_CONTAGEM = 3
MSG_CONTINUAR = 4
MSG_FIM = 5


def enviar_mensagem(sock, tipo, corpo=b""):
    """
    Envia uma mensagem completa pelo socket, com prefixo de tamanho.

    Parâmetros:
        sock (socket.socket): socket TCP conectado.
        tipo (int): um dos MSG_*.
        corpo (bytes): conteúdo já serializado.

    Retorno:
        None. Deve usar sendall para garantir o envio completo.
    """
    # TODO: montar cabeçalho com struct.pack e usar sock.sendall
    raise NotImplementedError


def receber_mensagem(sock):
    """
    Recebe uma mensagem completa do socket.

    Parâmetros:
        sock (socket.socket): socket TCP conectado.

    Retorno:
        tuple[int, bytes]: (tipo, corpo).
        Deve tratar leituras parciais (recv pode devolver menos bytes) e a
        conexão fechada pelo outro lado.
    """
    # TODO: implementar helper de leitura exata (_receber_exato)
    raise NotImplementedError


def serializar_linhas(linhas):
    """
    Converte uma ou mais linhas da grade (listas de inteiros 0..2) em bytes.

    Parâmetros:
        linhas (list[list[int]]): linhas a enviar (ex.: uma linha de halo).

    Retorno:
        bytes: representação compacta (ex.: 1 byte por célula, ou bitmask).
    """
    # TODO: implementar (decidir se inclui nº de linhas/colunas no corpo)
    raise NotImplementedError


def desserializar_linhas(dados, colunas):
    """
    Operação inversa de serializar_linhas.

    Parâmetros:
        dados (bytes): corpo recebido.
        colunas (int): número de colunas de cada linha.

    Retorno:
        list[list[int]]: linhas reconstruídas.
    """
    # TODO: implementar
    raise NotImplementedError


def serializar_contagem(contagem):
    """
    Converte a contagem {IGNORANTE, ESPALHADOR, INATIVO} em bytes (struct).

    Retorno:
        bytes.
    """
    # TODO: implementar
    raise NotImplementedError


def desserializar_contagem(dados):
    """
    Operação inversa de serializar_contagem.

    Retorno:
        dict[int, int]: {IGNORANTE: n, ESPALHADOR: n, INATIVO: n}.
    """
    # TODO: implementar
    raise NotImplementedError
