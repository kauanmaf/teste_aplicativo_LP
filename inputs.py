from converte_data import receber_datas, converter_data
from le_arquivo_texto import ler_texto
from calculo_data import calculo_datas
import datetime


def get_type_input():
    """
    Função para receber inputs e returnar o usuário com a diferença de tempo entre strings
    """

    # Decidindo qual o tipo de arquivo
    type_input = input("Você deseja:\n ler um arquivo [1] ou digitar uma string [2]: ")


    try: 
        # Se for um arquivo
        if type_input == "1":

            # Pegando o nome do arquivo
            txt_com_datas = input("Digite o nome do arquivo: ")

            # Tratando se o erro não for um arquivo de texto
            if txt_com_datas[-4:] != ".txt":
                raise ValueError
            
            # Pegando a string no formato especificado
            string_com_datas = ler_texto(txt_com_datas)

        # Se for uma string
        if type_input == "2":

            # Pegando a string no formato especificado
            string_com_datas = input("Digite a string com as datas: ")
    
    except ValueError:
        # tratando exceção levantada
        print("O formato não é um arquivo de texto")
    except:
        # Tratando alguma outra exceção
        print("Ocorreu algum outro erro")

    else:
        # Pegando uma lista com datas
        list_with_dates = receber_datas(string_com_datas)

        # Pegando todas as datas
        primeira_data = converter_data(list_with_dates[0])
        segunda_data = converter_data(list_with_dates[1])

        # Pegando as diferenças de data
        diferença_de_datas = calculo_datas(primeira_data, segunda_data)

        # Retornando a diferença
        return diferença_de_datas