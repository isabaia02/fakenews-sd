"""
Testes de equivalência: paralelo e distribuído == sequencial.

Critério: com os mesmos parâmetros e a MESMA semente, as contagens por geração
(ignorantes, espalhadores, inativos) devem ser idênticas às da versão
sequencial. Usar grades pequenas para os testes serem rápidos.

Executar: python -m unittest discover tests

Responsável: A definir
"""

import unittest

from fakenews import sequencial  # noqa: F401


class TestEquivalenciaParalelo(unittest.TestCase):
    """Compara as versões paralelas com a sequencial."""

    def test_threads_igual_sequencial(self):
        """Versão com threading gera as mesmas contagens por geração."""
        self.skipTest("TODO: implementar")

    def test_multiprocessing_igual_sequencial(self):
        """Versão com multiprocessing gera as mesmas contagens por geração."""
        self.skipTest("TODO: implementar")

    def test_paralelo_varios_numeros_de_workers(self):
        """Resultado independe do nº de workers (1, 2, 3, 4...), inclusive
        quando o nº de linhas não é divisível pelo nº de workers."""
        self.skipTest("TODO: implementar")


class TestEquivalenciaDistribuido(unittest.TestCase):
    """Compara a versão distribuída com a sequencial."""

    def test_distribuido_igual_sequencial(self):
        """Coordenador + trabalhadores (localhost) geram as mesmas contagens."""
        self.skipTest("TODO: implementar")

    def test_distribuido_varios_numeros_de_trabalhadores(self):
        """Resultado independe do nº de trabalhadores (testa o halo exchange
        nas fronteiras entre faixas)."""
        self.skipTest("TODO: implementar")

    def test_parada_antecipada_sem_espalhadores(self):
        """Todas as versões param na mesma geração quando não há espalhadores."""
        self.skipTest("TODO: implementar")


if __name__ == "__main__":
    unittest.main()
