import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host="127.0.0.1",
        port="8888",
        user="root",
        passwd="root",
        unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', # Para conectar a la base de datos en MacOS o Linux
        database="master_python"
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]