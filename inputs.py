from ferramentas import receber_datas, converter_data, ler_texto, calculo_datas
import datetime
import doctest

def get_type_input():
    """
    Função para receber inputs e returnar o usuário com a diferença de tempo entre strings

    Retorna um lista com a diferença de dias.

    >>> Get_type_input()
    >>> 1
    >>> Nome.txt
    >>> 11
    """

    # Decidindo qual o tipo de arquivo
    type_input = input("Você deseja:\nLer um arquivo [1] ou digitar uma string [2]: ")


    try: 
        # Se for um arquivo
        if type_input == "1":

            # Pegando o nome do arquivo
            txt_com_datas = input("Digite o nome do arquivo: ")

            # Tratando se o erro não for um arquivo de texto
            if txt_com_datas[-4:] != ".txt":
                raise ValueError
            
            # Pegando a string no formato especificado
            lista_com_datas = ler_texto(txt_com_datas)

        # Se for uma string
        if type_input == "2":

            # Pegando a string no formato especificado
            lista_com_datas = []
            data = input("Digite a string com as datas: ")
            lista_com_datas.append(data)
    
    except ValueError:
        # tratando exceção levantada
        print("O formato não é um arquivo de texto")
    except:
        # Tratando alguma outra exceção
        print("Ocorreu algum outro erro")

    else:
        # Diferenças de dias:
        lista_diferenca_de_data = []
        for string in lista_com_datas:
            # Pegando uma lista com datas
            list_with_dates = receber_datas(string)

            # Pegando todas as datas
            primeira_data = converter_data(list_with_dates[0])
            segunda_data = converter_data(list_with_dates[1])

            # Pegando as diferenças de data
            diferença_de_datas = calculo_datas(primeira_data, segunda_data)

            # Adicionando a lista
            lista_diferenca_de_data.append(diferença_de_datas)

        # Retornando a diferença
        return lista_diferenca_de_data  
    
    if __name__ == "__name__":
        doctest.testmod(verbose=True)
        print("teste concluído")

get_type_input()