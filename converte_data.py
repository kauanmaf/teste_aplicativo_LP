import doctest


def receber_datas(datas: str):
    """
    Recebe duas strings de datas separadas por um - e as devolve em uma lista
    separadamente.

    Parameters
    ----------
    datas: str
        String com duas datas a serem separadas.

    Returns
    -------
    sep_datas: list
        Lista com as duas datas separadas.

    Teste simples que já deve ser geral para qualquer caso
    >>> receber_datas("29 de Janeiro de 2005 - 25 de Março de 2003")
    ['29 de Janeiro de 2005', '25 de Março de 2003']
    """
    sep_datas = datas.split(" - ")
    return sep_datas


def converter_data(data: str):
    """
    Recebe uma string de data da forma "dia de mes(nome do mes) de ANO" e retorna no formato de
    "ANO-mes-dia".

    Parameters
    ----------
    data: str
        String da data a ser convertida.
    
    Returns
    -------
    new_format: str
        A string com a data do formato requerido

    Exemplo simples da função para testar, como o tratamento foi feito no
    input do usuário não deve ser necessário fazer tratamento extra.
    
    >>> converter_data("29 de Janeiro de 2005")
    '2005-01-29'
    """
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

    new_format = ano + "-" + mes_num + "-" + dia

    return new_format


if __name__ == "__main__":
    doctest.testmod(verbose=True)

