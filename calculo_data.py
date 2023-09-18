""" Documentação do módulo

    Este móduo contém a função calculo_datas, que retorna o número de dias entre duas datas.

"""


import datetime
import doctest

def calculo_datas(data1, data2):
    """ Cálculo da diferença entre datas

    Parameters
    ----------
    data1 : string
        string contendo o formato necessário para o cálculo 
    data2 : string
        string contendo o formato necessário para o cálculo 

    Returns
    -------
    calculo : int
        retorna o valor absoluto da diferença entre as duas datas
        
    Exemplo:
        Usando um par de datas com todos os três elementos diferentes afim testar os código.
    >>> calculo_datas("2004-06-18", "2006-10-25")
    O número de dias de diferença é: 859
    859
    
    """
    # Transforma as strings em objetos da biblioteca datetime
    d1 = datetime.datetime.strptime(data1,"%Y-%m-%d" )
    d2 = datetime.datetime.strptime(data2,"%Y-%m-%d")
    
    # Calcula do valor absoluto da diferença entre as datas
    calculo = abs((d2 - d1).days)
    
    print("O número de dias de diferença é:", calculo)
    
    return calculo

if __name__ == "__main__":
    doctest.testmod(verbose = True)
    print("Teste concluído")


