from converte_data import receber_datas, converter_data
from le_arquivo_texto import ler_texto
from calculo_data import calculo_datas
import datetime


def get_type_input():
    """
    função para receber inputs e returnar o Usuário com strings formatadas
    """

    # Decidindo qual o tipo de arquivo
    type_input = input("Você deseja:\n ler um arquivo [1] ou digitar uma string [2]: ")


    try: 
        # Se for um arquivo
        if type_input == "1":
            txt_com_datas = input("Digite o nome do arquivo: ")
            if txt_com_datas[-4:] != ".txt":
                raise ValueError
            string_com_datas = ler_texto(txt_com_datas)

        # Se for uma string
        if type_input == "2":
            string_com_datas = input("Digite a string com as datas: ")
    except ValueError:
        print("O formato não é um arquivo de texto")
    except:
        print("Ocorreu algum outro erro")

    else:
        list_with_dates = receber_datas(string_com_datas)
        primeira_data = converter_data(list_with_dates[0])
        segunda_data = converter_data(list_with_dates[1])
        diferença_de_datas = calculo_datas(primeira_data, segunda_data)
        return diferença_de_datas

get_type_input()

