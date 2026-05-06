import sqlite3 
import pandas as pd

def criar_conexao(name = 'vendas_games.db') : 
    '''
    aqui será criado a conexão com o banco de dados 
    '''
    conn = sqlite3.connect(name)
    return conn 

def carregar_csv_to_sql(caminho_csv, name_tabela, conn) : 
    df = pd.read_csv(caminho_csv)

    df.to_sql(name_tabela, conn, if_exists = 'replace', index = False)
    print (f'Sucesso: tabela <{name_tabela}> criada com {len(df)} registros.')

if __name__ == '__main__':
    conexao = criar_conexao()
    carregar_csv_to_sql('Data/vgsales.csv','vendas', conexao)
    conexao.close()