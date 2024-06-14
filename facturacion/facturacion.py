from datetime import datetime

import sys
import os

ruta_conexion_bd = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","conexion"))
sys.path.append(ruta_conexion_bd)
from conexion_bd import cerrar, obtener_conexion



def obtener_datos_empresa():
    # Datos de la empresa (puedes modificar estos datos según sea necesario)
    return {
        "nombre": "Nombre de la Empresa",
        "cif_nie": "CIF_NIE de la Empresa",
        "direccion": "Dirección de la Empresa",
        "cpgit ": "Código Postal de la Empresa",
        "provincia": "Provincia de la Empresa"

    }

def obtener_datos_cliente(nif):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "SELECT nombre, apellido, direccion, codigopostal, provincia FROM cliente WHERE nif_nie = %s"
    cursor.execute(sql, (nif,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()
    return {
        "nombre": resultado[0],
        "apellido": resultado[1],
        "direccion": resultado[2],
        "codigo_postal": resultado[3],
        "provincia": resultado[4]
    }

def obtener_precio_unitario(producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "SELECT precio_unitario FROM productos WHERE nombre = %s"
    cursor.execute(sql, (producto,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()
    return resultado[0] if resultado else None

def obtener_datos_productos():
    productos = []
    while True:
        producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if producto.lower() == 'fin':
            break
        cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
        precio_unitario = obtener_precio_unitario(producto)
        if precio_unitario is None:
            print(f"El producto '{producto}' no se encontró en la base de datos.")
            continue
        total = cantidad * precio_unitario
        productos.append({
            "producto": producto,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "total": total
        })
    return productos

def calcular_total_general(productos):
    total_general = sum(producto['total'] for producto in productos)
    return total_general, total_general * 1.21  # 21% IVA

def facturacion():
    datos_empresa = obtener_datos_empresa()
    nif_cliente = input("Introduce el NIF/NIE del cliente: ")
    datos_cliente = obtener_datos_cliente(nif_cliente)
    fecha_factura = datetime.now().strftime("%d/%m/%Y")
    productos = obtener_datos_productos()
    total_general, total_con_iva = calcular_total_general(productos)

    print("\n--- FACTURA ---")
    print(f"Fecha: {fecha_factura}\n")
    print("Datos de la Empresa:")
    for key, value in datos_empresa.items():
        print(f"{key}: {value}")

    print("\nDatos del Cliente:")
    for key, value in datos_cliente.items():
        print(f"{key}: {value}")

    print("\nLíneas de Factura:")
    for producto in productos:
        print(f"Producto: {producto['producto']}, Cantidad: {producto['cantidad']}, Precio Unitario: {producto['precio_unitario']:.2f}, Total: {producto['total']:.2f}")

    print(f"\nTotal General: {total_general:.2f}")
    print(f"Total con IVA (21%): {total_con_iva:.2f}")

    input("\nPresione Enter para continuar...")

# Ejecutar la función para generar la factura

