import mysql.connector
from mysql.connector import Error


def obtener_conexion():
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="datos_2"  # Especifica el nombre de tu base de datos aquí
    )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos.")
            return connection
    except Error as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None

def cerrar(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Conexion Cerrada")