import numpy as np 

def porcentagem_regional(parte , total, casas = 2): ##Aqui temos a "Parte" que seria basicamente o número de obitos que ocorreram e o "Total" que seria basicamente o total do recorte óbito pelo local 
    calculo = np.where(total > 0, (parte / total) * 100, 0) ## Aqui aplicamos a regra do "TOTAL > 0" para evitarmos divisão por 0 ou valor negativo. Se for tudo certo, será um cálculo de porcentagem comum
    ## Parte(Num_obito)/ Total(Num_total_casos)* e multiplicamos por 100% que seria o valor de tudo. 
    np.round(calculo, casas) ##Aqui a gente arredonda o valor do resultado do nosso calculo para que ele não fique com número quebrado e traz apena as duas primeiras casas após a virgula