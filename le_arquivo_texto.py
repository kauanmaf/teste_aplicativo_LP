
def ler_texto(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        data = arquivo.read().strip()
    return data


