import pandas as pd
import matplotlib.pyplot as plt

def leitura_dados (arquivo) :
    df = pd.read_csv(arquivo)
    return df

def info_geral(df) :
    """
    Gera um resumo de todos os valores contidos nos dados
    """
    return df.info()

def limpeza_dados(df) :
    return df.fillna("Desconhecido")

def total_linhas_colunas(df):
    return df.shape

def vizu_dados_faltantes (df) :
    """
    Encontrando onde os dados faltantes estão, através de gráficos
    """
    contagem_ausentes = df.isnull().sum()
    contagem_ausentes = contagem_ausentes[contagem_ausentes > 0 ]
    if not contagem_ausentes.empty :
        contagem_ausentes.plot(kind='bar' , figsize=(10,6))
        plt.title('Contagem de valores ausentes do dataset VG.SALES_CSV')
        plt.xlabel('Colunas')
        plt.ylabel('Contagem de valores ausentes')
        plt.show()
    else :
        print ("Não há valores ausentes...")
   