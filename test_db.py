import mysql.connector
from config import DATABASE_CONFIG

def test_connection():
    try:
        db = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()
        print(f"Conectado ao banco de dados: {db_name}")
        cursor.close()
        db.close()
        print("Conexão ao banco de dados foi bem-sucedida.")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")

if __name__ == "__main__":
    test_connection()
