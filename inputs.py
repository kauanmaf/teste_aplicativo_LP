from converte_data import receber_datas, converter_data

def get_type_input():
    type_input = input("Você deseja: \n ler um arquivo [1] \n digitar uma string [2]")
    if type_input == 1:

    if type_input == 2:
        string_com_datas = input("Digite a string com as datas: ")
        list_with_dates = receber_datas(string_com_datas)
        primeira_data = converter_data(list_with_dates[0])
        segunda_data = converter_data(list_with_dates[1])
        

