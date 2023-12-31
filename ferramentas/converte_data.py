""" Documentação do módulo
    
    Este módulo recebe as datas do usuário no formato string "DIA de MÊS de ANO - DIA de MÊS de ANO".
    Então, ele divide as datas em duas strings e muda o jeito como estão escritas, de nomes para números que identificam os meses com um dicionário.
    Ele prepara as strings do usuário para o cálculo em outros módulos.
"""

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
    "ANO-mes-dia", alguns tratamentos como para verificar se foram recebidos um dia, mês e ano
    ou se o mês é válido foram deferidos.

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
    lista_meses = list(meses.keys())

    try:
        sep_data = data.split(" de ")
        if len(sep_data) != 3 or sep_data[1].capitalize() not in lista_meses:
            raise TypeError
    except ValueError:
        print("Tente inserir uma string!")
    except TypeError:
        print("Formato de data requierido está incorreto!\nUm exemplo seria '29 de Janeiro de 2005'")

    dia = sep_data[0]
    mes = sep_data[1].capitalize()
    ano = sep_data[2]

    mes_num = meses[mes]

    new_format = ano + "-" + mes_num + "-" + dia

    return new_format


if __name__ == "__main__":
    doctest.testmod(verbose=True)

