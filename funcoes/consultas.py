import pandas as pd


##Aqui estou fazendo uma consulta básica de dados da tabela completa
def consulta_completa(conn):
    query_completa = """
    SELECT * FROM
    ODS_COVID_ESTADOS;"""
    return pd.read_sql_query(query_completa, conn)

##Aqui estou fazendo uma consulta para trazer o máximo de número de obito e agrupado por cada estado 
def consulta_maxima(conn):
    query_maximo_obito = """
    SELECT
    NME_ESTADO_OCORRIDO,
    MAX(NUM_OBITO) AS TOTAL_OBITOS
    FROM ODS_COVID_ESTADOS
    GROUP BY NME_ESTADO_OCORRIDO
    ORDER BY TOTAL_OBITOS DESC;"""
    return pd.read_sql_query(query_maximo_obito, conn)

##Aqui estou fazendo um consulta básica de count da tabela para verificação de conteúdo, 
def consulta_count(conn):
    query_contagem = """
    SELECT COUNT(*)
    FROM ODS_COVID_ESTADOS; 
    """
    return pd.read_sql_query(query_contagem, conn)