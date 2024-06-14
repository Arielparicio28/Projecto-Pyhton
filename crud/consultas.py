import sys
import os


ruta_conexion_bd = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","conexion"))
sys.path.append(ruta_conexion_bd)
from conexion_bd import obtener_conexion


def consultas(tabla):
    conexion = obtener_conexion()
    if conexion is None:
        print("No se pudo establecer la conexión a la base de datos.")
        return
    
    try:
        cursor = conexion.cursor()
 
    # Tabla Clientes
        if tabla == "1":
            nif = input("Introduce tu Nif/Nie: ")
            sql = "SELECT * FROM cliente WHERE nif_nie = %s"
            cursor.execute(sql, (nif,))
            resultado = cursor.fetchall()
            for cliente in resultado:
                print(f"Nombre: {cliente[1]}, Apellido: {cliente[2]}, Dirección: {cliente[4]}, Código Postal: {cliente[5]}, Provincia: {cliente[6]}")
    
    # Tabla Código Postal
        if tabla == "2":
            codigo = input("Escriba un código postal: ")
            sql = "SELECT * FROM codigopostal WHERE codigo = %s"
            cursor.execute(sql, (codigo,))
            resultado = cursor.fetchall()
            for codigopostal in resultado:
                print(f"Código: {codigopostal[1]}, Descripción: {codigopostal[2]}")
    
    # Tabla Población
        if tabla == "3":
            codigoP = input("Escriba un código postal: ")
            sql = "SELECT * FROM poblacion WHERE codigo = %s"
            cursor.execute(sql, (codigoP,))
            resultado = cursor.fetchall()
            for poblacion in resultado:
                print(f"Código: {poblacion[1]}, Descripción: {poblacion[2]}")

    # Tabla Provincias
        if tabla == "4":
            codigoPro = input("Escriba un código postal: ")
            sql = "SELECT * FROM provincias WHERE codigo = %s"
            cursor.execute(sql, (codigoPro,))
            resultado = cursor.fetchall()
            for provincia in resultado:
                print(f"Código: {provincia[1]}, Descripción: {provincia[2]}")
    
    # Tabla Banco
        if tabla == "5":
            nombreBanco = input("Escriba el nombre de su banco: ")
            sql = "SELECT * FROM bancos WHERE nombre_entidad = %s"
            cursor.execute(sql, (nombreBanco,))
            resultado = cursor.fetchall()
            for banco in resultado:
                print(f"Nombre del Banco: {banco[1]}, IBAN: {banco[2]}, SWIFT: {banco[3]}")

    # Tabla Dirección Envío
        if tabla == "6":
            codigoPosenvio = input("Escriba el código de envío: ")
            sql = "SELECT * FROM direccionenvio WHERE codigo_postal = %s"
            cursor.execute(sql, (codigoPosenvio,))
            resultado = cursor.fetchall()
            for direccion in resultado:
                print(f"Código Postal: {direccion[1]}, Población: {direccion[2]}, Provincia: {direccion[3]}")

    except Exception as e:
        print("Error al consultar datos: ", e)
    finally:
        cursor.close()
        conexion.close()
    input("Presione Enter para continuar...")
