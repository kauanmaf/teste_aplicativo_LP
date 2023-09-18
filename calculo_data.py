import datetime

def calculo_datas(data1, data2):
    d1 = datetime.datetime.strptime(data1,"%Y-%m-%d" )
    d2 = datetime.datetime.strptime(data2,"%Y-%m-%d")
    
    calculo = abs((d2 - d1).days)
    
    print("O número de dias de diferença é:", calculo)
    
    return calculo

calculo_datas("2004-05-07", "2004-06-23")






