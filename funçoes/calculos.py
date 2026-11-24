import numpy as np 

def porcentagem_regional(parte , total, casas = 2):
    calculo = np.where(total > 0, (parte / total) * 100, 0)
    np.round(calculo, casas)