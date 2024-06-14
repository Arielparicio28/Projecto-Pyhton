import sys
import os


ruta_conexion_bd = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","conexion"))
sys.path.append(ruta_conexion_bd)
from conexion_bd import obtener_conexion, cerrar


def baja(tabla):
    conexion = obtener_conexion()
    print(f"Valor de tabla, {tabla}")
    if conexion is None:
        print("No se pudo establecer la conexión a la base de datos.")
        return

    try:
        cursor = conexion.cursor()
 
    # Tabla Clientes
        if tabla == "1":
            nif = input("Introduce el Nif/Nie del cliente a eliminar: ")
            sql = "DELETE FROM cliente WHERE nif_nie = %s"
            valores = (nif,)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Cliente eliminado exitosamente.")
    
    # Tabla código postal
        if tabla == "2":
            codigo = input("Escriba el código postal a eliminar: ")
            sql = "DELETE FROM codigopostal WHERE codigo = %s"
            valores = (codigo,)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Código postal eliminado correctamente.")
    
    # Tabla población
        if tabla == "3":
            codigoP = input("Escriba el código postal de la población a eliminar: ")
            sql = "DELETE FROM poblacion WHERE codigo = %s"
            valores = (codigoP,)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Población eliminada correctamente.")

    # Tabla provincias
        if tabla == "4":
            codigoPro = input("Escriba el código postal de la provincia a eliminar: ")
            sql = "DELETE FROM provincias WHERE codigo = %s"
            valores = (codigoPro,)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Provincia eliminada correctamente.")
    
    # Tabla banco
        if tabla == "5":
            iban = input("Escriba el número de cuenta (IBAN) del banco a eliminar: ")
            sql = "DELETE FROM bancos WHERE codigo_iban = %s"
            valores = (iban,)
            cursor.execute(sql, valores)
            conexion.commit()
            +print("Banco eliminado correctamente.")

    # Tabla dirección de envío
        if tabla == "6":
            codigoPosenvio = input("Escriba el código postal de envío a eliminar: ")
            sql = "DELETE FROM direccionenvio WHERE codigo_postal = %s"
            valores = (codigoPosenvio,)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Dirección de envío eliminada correctamente.")

    except Exception as e:
        print("Error al eliminar datos: ", e)
    finally:
        cursor.close()
        cerrar(conexion)

if __name__ == "__main__":
    tabla = input("Seleccione la tabla en la que desea eliminar datos: \n1. Clientes\n2. Codigo Postal\n3. Poblacion\n4. Provincias\n5. Banco\n6. Dirección de envio\n")
    baja(tabla)