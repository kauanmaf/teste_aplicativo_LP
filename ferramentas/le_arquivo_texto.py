""" Documentação de módulo 

Este módulo define a função ler_texto, que transforma o arquivo .txt 
enviado pelo usuário em uma string a ser utilizada no cálculo em outros módulos.

"""


def ler_texto(nome_arquivo: str):
    """Função que lê datas de um arquivo de texto, as datas devem estar como:
    "dd" de "MM"(Nome do Mês) de "YYYY" - "dd" de "MM"(Nome do Mês) de "YYYY".
    Sendo que se houver mais de um par de datas, deve estar em outra linha.

    Args:
        nome_arquivo: str
            Nome do arquivo .txt com as datas selecionadas.

    Returns:
        datas: list
            Uma lista com cada um dos pares de datas lidos em cada linha.
    """
    with open(nome_arquivo, "r") as arquivo:
        datas = arquivo.read().splitlines()
    return datas

