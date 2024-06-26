import sys
import os

ruta_conexion_bd = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "conexion"))
sys.path.append(ruta_conexion_bd)

from conexion_bd import cerrar, obtener_conexion

def alta(tabla):
    conexion = obtener_conexion()
    print(f"Valor de tabla, {tabla}")
    if conexion is None:
        print("No se pudo establecer la conexión a la base de datos.")
        return

    try:
        cursor = conexion.cursor()

        # Tabla Clientes
        if tabla == "Clientes":
            codigo_cliente = input("Codigo de cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            nif_nie = input("Introduce tu NIF/NIE: ")
            direccion = input("Introduce tu dirección: ")
            codigoPostal = input("Introduce tu código postal: ")
            poblacion = input("Introduce la población en la que vives: ")
            provincia = input("Introduce tu provincia: ")

            sql = "INSERT INTO cliente (codigo_cliente,nombre, apellido, nif_nie, direccion, cp, poblacion, provincia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            valores = (codigo_cliente,nombre, apellido, nif_nie, direccion, codigoPostal, poblacion, provincia)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Cliente agregado exitosamente.")

        # Tabla Código Postal
        if tabla == "Codigo Postal":
            codigo = input("Escriba un código postal: ")
            descripcion = input("Escriba una descripción: ")

            sql = "INSERT INTO codigopostal (codigo, descripcion) VALUES (%s, %s)"
            val = (codigo, descripcion)
            cursor.execute(sql, val)
            conexion.commit()
            print("Datos introducidos correctamente.")

        # Tabla Población
        if tabla == "Poblacion":
            codigo = input("Escriba un código postal: ")
            descripcion = input("Escriba una descripción: ")

            sql = "INSERT INTO poblacion (codigo, descripcion) VALUES (%s, %s)"
            val = (codigo, descripcion)
            cursor.execute(sql, val)
            conexion.commit()
            print("Datos introducidos correctamente.")

        # Tabla Provincias
        if tabla == "Provincias":
            codigo = input("Codigo de provincia: ")
            descripcion = input("Escriba una descripción: ")

            sql = "INSERT INTO provincias (codigo, descripcion) VALUES (%s, %s)"
            val = (codigo, descripcion)
            cursor.execute(sql, val)
            conexion.commit()
            print("Datos introducidos correctamente.")

        # Tabla Banco
        if tabla == "Entidades Bancarias":
            codigo = input("escriba el codigo de su banco: ")
            nombreBanco = input("Escriba el nombre de su banco: ")
            iban = input("Escriba el número de cuenta: ")
            swift = input("Escriba el código internacional: ")

            sql = "INSERT INTO bancos (codigo_banco,nombre_entidad, codigo_iban, codigo_swift) VALUES (%s,%s, %s, %s)"
            val = (codigo,nombreBanco, iban, swift)
            cursor.execute(sql, val)
            conexion.commit()
            print("Datos introducidos correctamente.")

        # Tabla Dirección Envío
        if tabla == "Direcciones de Envío":
            codigoPosenvio = input("Escriba el código de envío: ")
            poblacionenvio = input("Escriba la población de envío: ")
            provinciaenvio = input("Escriba la provincia de envío: ")

            sql = "INSERT INTO direccionenvio (cp, poblacion, provincia) VALUES (%s, %s, %s)"
            val = (codigoPosenvio, poblacionenvio, provinciaenvio)
            cursor.execute(sql, val)
            conexion.commit()
            print("Datos introducidos correctamente.")

    except Exception as e:
        print("Error al insertar datos: ", e)
    finally:
        cursor.close()
        cerrar(conexion)

if __name__ == "__main__":
    tabla = input("Seleccione la tabla en la que desea insertar datos: \n1. Clientes\n2. Codigo Postal\n3. Poblacion\n4. Provincias\n5. Banco\n6. Dirección de envio\n")
    alta(tabla)
