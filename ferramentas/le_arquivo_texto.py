""" Documentação de módulo 

Este módulo define a função ler_texto, que transforma o arquivo .txt 
enviado pelo usuário em uma string a ser utilizada no cálculo em outros módulos.

"""


def ler_texto(nome_arquivo):
    """Função que lê datas de um arquivo de texto

    Args:
        nome_arquivo (_type_): _description_

    Returns:
        list: Uma lista com cada
    """
    with open(nome_arquivo, "r") as arquivo:
        datas = arquivo.read().splitlines()
    return datas

