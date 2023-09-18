""" Documentação de módulo 

Este módulo define a função ler_texto, que transforma o arquivo .txt 
enviado pelo usuário em uma string a ser utilizada no cálculo em outros módulos.

"""


def ler_texto(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        data = arquivo.read().strip()
    return data


