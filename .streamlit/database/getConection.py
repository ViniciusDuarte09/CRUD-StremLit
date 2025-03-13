import mysql.connector

def connect():
    
    try:
        con = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'streamlit')
        
        return con
    
    except:
        print("Erro ao realizar a conexão...")