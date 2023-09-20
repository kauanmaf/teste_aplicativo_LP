import unittest

from ferramentas import converte_data, le_arquivo_texto

class testandoMain(unittest.TestCase):
    def test_recebe_datas_1(self):
        with self.assertRaises(Exception):
            converte_data.receber_datas("çkldasfjçsklafjçlkas")

    def teste_recebe_data_2(self):
        with self.assertRaises(Exception):
            converte_data.receber_datas("0 de janeiro de 2022 - 0 de janeiro de 2023")

    def teste_recebe_data_3(self):
        with self.assertRaises(Exception):
            converte_data.receber_datas("-2 de janeiro de 2022 - -2 de janeiro de 2023")

    def teste_recebe_data_4(self):
        with self.assertRaises(Exception):
            assert(converte_data.receber_datas("1 de janeiro de 2022 - 1 de janeiro de 2022")) == 0

    def teste_recebe_data_5(self):
        with self.assertRaises(Exception):
            assert(converte_data.receber_datas("1 de janeiro de 28 - 1 de janeiro de 29")) == 365

    def teste_recebe_data_6(self):
        with self.assertRaises(Exception):
            converte_data.receber_datas("29 de fevereiro 2022 - 30 de fevereiro de 2022")

    def teste_converter_data(self):
        with self.assertRaises(Exception):
            converte_data.converter_data("oi de janeiro de opa")

    def test_arquivo_errado_1(self):
        with self.assertRaises(Exception):
            le_arquivo_texto.ler_texto("arquivo_errado.txt")

    def test_arquivo_errado_2(self):
        with self.assertRaises(Exception):
            le_arquivo_texto.ler_texto("will-careca.jfif")

    


if __name__ == "__main__":
    unittest.main(exit=False)