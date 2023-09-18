
def receber_datas(datas):
    sep_datas = datas.split(" - ")
    return sep_datas

def converter_data(data):
    meses = {
        "Janeiro": "01",
        "Fevereiro": "02",
        "Março": "03",
        "Abril": "04",
        "Maio": "05",
        "Junho": "06",
        "Julho": "07",
        "Agosto": "08",
        "Setembro": "09",
        "Outubro": "10",
        "Novembro": "11",
        "Dezembro": "12"
}

    sep_data = data.split(" de ")
    dia = sep_data[0]

    mes = sep_data[1]
    mes_num = meses[mes]

    ano = sep_data[2]

    new_format = ano + mes_num + dia

    return new_format



