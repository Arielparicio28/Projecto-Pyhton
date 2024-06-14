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
        if tabla == "Clientes":
            nif = input("Introduce tu codigo_cliente: ")
            sql = "SELECT * FROM cliente WHERE codigo_cliente = %s"
            cursor.execute(sql, (nif,))
            resultado = cursor.fetchall()
            for cliente in resultado:
                print(f"Nombre: {cliente[0]}, Apellido: {cliente[1]}, Dirección: {cliente[2]}, Código Postal: {cliente[3]}, Provincia: {cliente[4]}")
    
    # Tabla Código Postal
        if tabla == "Codigo Postal":
            codigo = input("Escriba un código postal: ")
            sql = "SELECT * FROM codigopostal WHERE codigo = %s"
            cursor.execute(sql, (codigo,))
            resultado = cursor.fetchall()
            for codigopostal in resultado:
                print(f"Código: {codigopostal[0]}, Descripción: {codigopostal[1]}")
    
    # Tabla Población
        if tabla == "Poblacion":
            codigoP = input("Escriba un código postal: ")
            sql = "SELECT * FROM poblacion WHERE codigo = %s"
            cursor.execute(sql, (codigoP,))
            resultado = cursor.fetchall()
            for poblacion in resultado:
                print(f"Código: {poblacion[0]}, Descripción: {poblacion[1]}")

    # Tabla Provincias
        if tabla == "Provincias":
            codigoPro = input("Escriba un código postal: ")
            sql = "SELECT * FROM provincias WHERE codigo = %s"
            cursor.execute(sql, (codigoPro,))
            resultado = cursor.fetchall()
            for provincia in resultado:
                print(f"Código: {provincia[0]}, Descripción: {provincia[1]}")
    
    # Tabla Banco
        if tabla == "Entidades Bancarias":
            nombreBanco = input("Escriba el nombre de su banco: ")
            sql = "SELECT * FROM bancos WHERE nombre_entidad = %s"
            cursor.execute(sql, (nombreBanco,))
            resultado = cursor.fetchall()
            for banco in resultado:
                print(f"Nombre del Banco: {banco[0]}, IBAN: {banco[1]}, SWIFT: {banco[2]}")

    # Tabla Dirección Envío
        if tabla == "Direcciones de Envío":
            codigoPosenvio = input("Escriba el código de envío: ")
            sql = "SELECT * FROM direccionenvio WHERE codigo_postal = %s"
            cursor.execute(sql, (codigoPosenvio,))
            resultado = cursor.fetchall()
            for direccion in resultado:
                print(f"Código Postal: {direccion[0]}, Población: {direccion[1]}, Provincia: {direccion[2]}")

    except Exception as e:
        print("Error al consultar datos: ", e)
    finally:
        cursor.close()
        conexion.close()
    input("Presione Enter para continuar...")
