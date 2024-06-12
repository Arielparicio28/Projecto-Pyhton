import mysql.connector
import os
from datetime import datetime

# Función para conectar a la base de datos
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="datos2"  # Especifica el nombre de tu base de datos aquí
    )

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar el menú principal
def menu_principal():
    while True:
        limpiar_pantalla()
        print("\nMenú Principal:")
        print("1. Mantenimiento")
        print("2. Facturación")
        print("3. Impresión de la Facturación")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_mantenimiento()
        elif opcion == "2":
            facturacion()
        elif opcion == "3":
            crear_factura()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Función para mostrar el menú de mantenimiento
def menu_mantenimiento():
    while True:
        limpiar_pantalla()
        print("\nMenú Mantenimiento:")
        print("1. Clientes")
        print("2. Codigo Postal")
        print("3. Poblacion")
        print("4. Provincias")
        print("5. Entidades Bancarias")
        print("6. Direcciones de Envío")
        print("7. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            submenu_tabla("Clientes")
        elif opcion == "2":
            submenu_tabla("Codigo Postal")
        elif opcion == "3":
            submenu_tabla("Poblacion")
        elif opcion == "4":
            submenu_tabla("Provincias")
        elif opcion == "5":
            submenu_tabla("Entidades Bancarias")
        elif opcion == "6":
            submenu_tabla("Direcciones de Envío")
        elif opcion == "7":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Función para mostrar el submenú de una tabla específica
def submenu_tabla(tabla):
    while True:
        limpiar_pantalla()
        print(f"\nMenú {tabla}:")
        print("1. Alta")
        print("2. Baja")
        print("3. Modificación")
        print("4. Consulta")
        print("5. Volver al Menú Mantenimiento")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta(tabla)
        elif opcion == "2":
            baja(tabla)
        elif opcion == "3":
            modificacion(tabla)
        elif opcion == "4":
            consulta(tabla)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Función para realizar el alta en una tabla específica
def alta(tabla):
    limpiar_pantalla()
    conexion = conectar()
    cursor = conexion.cursor()

    if tabla == "Clientes":
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        nif = input("Introduce tu Nif/Nie: ")
        direccion = input("Introduce tu dirección: ")
        codigoPostal = input("Introduce tu codigo postal: ")
        poblacion = input("Introduce la poblacion en la que vives: ")
        provincia = input("Introduce tu provincia: ")
       
        sql = "INSERT INTO cliente (nombre, apellido, nif_nie, direccion, cp, poblacion, provincia) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (nombre, apellido, nif, direccion, codigoPostal, poblacion, provincia)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Cliente agregado exitosamente.")
    
    elif tabla == "Codigo Postal":
        codigo = input("Escriba un código postal: ")
        descripcion = input("Escriba una descripción: ")
      
        sql = "INSERT INTO codigopostal (codigo, descripcion) VALUES (%s, %s)"
        valores = (codigo, descripcion)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Datos introducidos correctamente.")
    
    elif tabla == "Poblacion":
        codigoP = input("Escriba un código postal: ")
        descripcionP = input("Escriba una descripción: ")
      
        sql = "INSERT INTO poblacion (codigo, descripcion) VALUES (%s, %s)"
        valores = (codigoP, descripcionP)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Datos introducidos correctamente.")

    elif tabla == "Provincias":
        codigoPro = input("Escriba un código postal: ")
        descripcionPro = input("Escriba una descripción: ")
      
        sql = "INSERT INTO provincias (codigo, descripcion) VALUES (%s, %s)"
        valores = (codigoPro, descripcionPro)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Datos introducidos correctamente.")
    
    elif tabla == "Entidades Bancarias":
        nombreBanco = input("Escriba el nombre de su banco: ")
        iban = input("Escriba el número de cuenta: ")
        swift = input("Escriba el código internacional: ")

        sql = "INSERT INTO bancos (nombre_entidad, codigo_iban, codigo_swift) VALUES (%s, %s, %s)"
        valores = (nombreBanco, iban, swift)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Datos introducidos correctamente.")

    elif tabla == "Direcciones de Envío":
        codigoPosenvio = input("Escriba el código postal de envío: ")
        poblacionenvio = input("Escriba la población de envío: ")
        provinciaenvio = input("Escriba la provincia de envío: ")

        sql = "INSERT INTO direccionenvio (cp, poblacion, provincia) VALUES (%s, %s, %s)"
        valores = (codigoPosenvio, poblacionenvio, provinciaenvio)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Datos introducidos correctamente.")

    cursor.close()
    conexion.close()
    input("Presione Enter para continuar...")

# Función para realizar la baja en una tabla específica
def baja(tabla):
    limpiar_pantalla()
    conexion = conectar()
    cursor = conexion.cursor()
 
    if tabla == "Clientes":
        nif = input("Introduce el Nif/Nie del cliente a eliminar: ")
        sql = "DELETE FROM cliente WHERE nif_nie = %s"
        valores = (nif,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Cliente eliminado exitosamente.")
    
    elif tabla == "Codigo Postal":
        codigo = input("Escriba el código postal a eliminar: ")
        sql = "DELETE FROM codigopostal WHERE codigo = %s"
        valores = (codigo,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Código postal eliminado correctamente.")
    
    elif tabla == "Poblacion":
        codigoP = input("Escriba el código postal de la población a eliminar: ")
        sql = "DELETE FROM poblacion WHERE codigo = %s"
        valores = (codigoP,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Población eliminada correctamente.")

    elif tabla == "Provincias":
        codigoPro = input("Escriba el código postal de la provincia a eliminar: ")
        sql = "DELETE FROM provincias WHERE codigo = %s"
        valores = (codigoPro,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Provincia eliminada correctamente.")
    
    elif tabla == "Entidades Bancarias":
        iban = input("Escriba el número de cuenta (IBAN) del banco a eliminar: ")
        sql = "DELETE FROM bancos WHERE codigo_iban = %s"
        valores = (iban,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Banco eliminado correctamente.")

    elif tabla == "Direcciones de Envío":
        codigoPosenvio = input("Escriba el código postal de envío a eliminar: ")
        sql = "DELETE FROM direccionenvio WHERE cp = %s"
        valores = (codigoPosenvio,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Dirección de envío eliminada correctamente.")

    cursor.close()
    conexion.close()
    input("Presione Enter para continuar...")

# Función para realizar la consulta en una tabla específica
def consulta(tabla):
    limpiar_pantalla()
    conexion = conectar()
    cursor = conexion.cursor()
 
    if tabla == "Clientes":
        nif = input("Introduce tu Nif/Nie: ")
        sql = "SELECT * FROM cliente WHERE nif_nie = %s"
        valores = (nif,)
        cursor.execute(sql, valores)
        cliente = cursor.fetchone()
        if cliente:
            print("Datos del cliente:")
            print(cliente)
        else:
            print("Cliente no encontrado.")
    
    elif tabla == "Codigo Postal":
        codigo = input("Escriba un código postal: ")
        sql = "SELECT * FROM codigopostal WHERE codigo = %s"
        valores = (codigo,)
        cursor.execute(sql, valores)
        cp = cursor.fetchone()
        if cp:
            print("Datos del código postal:")
            print(cp)
        else:
            print("Código postal no encontrado.")
    
    elif tabla == "Poblacion":
        codigoP = input("Escriba un código postal: ")
        sql = "SELECT * FROM poblacion WHERE codigo = %s"
        valores = (codigoP,)
        cursor.execute(sql, valores)
        poblacion = cursor.fetchone()
        if poblacion:
            print("Datos de la población:")
            print(poblacion)
        else:
            print("Población no encontrada.")

    elif tabla == "Provincias":
        codigoPro = input("Escriba un código postal: ")
        sql = "SELECT * FROM provincias WHERE codigo = %s"
        valores = (codigoPro,)
        cursor.execute(sql, valores)
        provincia = cursor.fetchone()
        if provincia:
            print("Datos de la provincia:")
            print(provincia)
        else:
            print("Provincia no encontrada.")
    
    elif tabla == "Entidades Bancarias":
        iban = input("Escriba el número de cuenta (IBAN): ")
        sql = "SELECT * FROM bancos WHERE codigo_iban = %s"
        valores = (iban,)
        cursor.execute(sql, valores)
        banco = cursor.fetchone()
        if banco:
            print("Datos del banco:")
            print(banco)
        else:
            print("Banco no encontrado.")

    elif tabla == "Direcciones de Envío":
        codigoPosenvio = input("Escriba el código postal de envío: ")
        sql = "SELECT * FROM direccionenvio WHERE cp = %s"
        valores = (codigoPosenvio,)
        cursor.execute(sql, valores)
        direccion = cursor.fetchone()
        if direccion:
            print("Datos de la dirección de envío:")
            print(direccion)
        else:
            print("Dirección de envío no encontrada.")

    cursor.close()
    conexion.close()
    input("Presione Enter para continuar...")

# Función para realizar la modificación en una tabla específica
def modificacion(tabla):
    limpiar_pantalla()
    conexion = conectar()
    cursor = conexion.cursor()

    if tabla == "Clientes":
        nif = input("Introduce tu Nif/Nie del cliente a modificar: ")
        nuevo_nombre = input("Introduce el nuevo nombre del cliente: ")
        nuevo_apellido = input("Introduce el nuevo apellido del cliente: ")
        nueva_direccion = input("Introduce la nueva dirección: ")
        nuevo_cp = input("Introduce el nuevo código postal: ")
        nueva_poblacion = input("Introduce la nueva población: ")
        nueva_provincia = input("Introduce la nueva provincia: ")
        sql = "UPDATE cliente SET nombre = %s, apellido = %s, direccion = %s, cp = %s, poblacion = %s, provincia = %s WHERE nif_nie = %s"
        valores = (nuevo_nombre, nuevo_apellido, nueva_direccion, nuevo_cp, nueva_poblacion, nueva_provincia, nif)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Cliente modificado exitosamente.")
    
    elif tabla == "Codigo Postal":
        codigo = input("Escriba el código postal a modificar: ")
        nueva_descripcion = input("Escriba la nueva descripción: ")
        sql = "UPDATE codigopostal SET descripcion = %s WHERE codigo = %s"
        valores = (nueva_descripcion, codigo)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Código postal modificado correctamente.")
    
    elif tabla == "Poblacion":
        codigoP = input("Escriba el código postal de la población a modificar: ")
        nueva_descripcionP = input("Escriba la nueva descripción: ")
        sql = "UPDATE poblacion SET descripcion = %s WHERE codigo = %s"
        valores = (nueva_descripcionP, codigoP)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Población modificada correctamente.")

    elif tabla == "Provincias":
        codigoPro = input("Escriba el código postal de la provincia a modificar: ")
        nueva_descripcionPro = input("Escriba la nueva descripción: ")
        sql = "UPDATE provincias SET descripcion = %s WHERE codigo = %s"
        valores = (nueva_descripcionPro, codigoPro)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Provincia modificada correctamente.")
    
    elif tabla == "Entidades Bancarias":
        iban = input("Escriba el número de cuenta (IBAN) del banco a modificar: ")
        nuevo_nombreBanco = input("Escriba el nuevo nombre del banco: ")
        nuevo_swift = input("Escriba el nuevo código internacional (SWIFT): ")
        sql = "UPDATE bancos SET nombre_entidad = %s, codigo_swift = %s WHERE codigo_iban = %s"
        valores = (nuevo_nombreBanco, nuevo_swift, iban)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Banco modificado correctamente.")

    elif tabla == "Direcciones de Envío":
        codigoPosenvio = input("Escriba el código postal de envío a modificar: ")
        nueva_poblacionenvio = input("Escriba la nueva población de envío: ")
        nueva_provinciaenvio = input("Escriba la nueva provincia de envío: ")
        sql = "UPDATE direccionenvio SET poblacion = %s, provincia = %s WHERE cp = %s"
        valores = (nueva_poblacionenvio, nueva_provinciaenvio, codigoPosenvio)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Dirección de envío modificada correctamente.")

    cursor.close()
    conexion.close()
    input("Presione Enter para continuar...")

# Función para realizar facturación
def facturacion():
    limpiar_pantalla()
    print("Función de facturación no implementada.")
    input("Presione Enter para continuar...")

# Función para crear una factura
def crear_factura():
    limpiar_pantalla()

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet

def create_invoice(pdf_path, logo_path):
    # Configuración del documento
    doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=20*mm, leftMargin=20*mm, topMargin=20*mm, bottomMargin=20*mm)
    elements = []
    
    # Estilos
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']
    
    # Logo
    logo = Image(logo_path, width=50*mm, height=50*mm)
    
    # Encabezado de la factura
    encabezado_data = [
        ['DE', 'N° DE FACTURA', 'ES-001'],
        ['Rojo Polo Paella Inc.', 'FECHA', '29/01/2019'],
        ['Carretera Muelle 38', 'N° DE PEDIDO', '1730/2019'],
        ['37531 Ávila, Ávila', 'FECHA VENCIMIENTO', '29/01/2019']
    ]
    encabezado_table = Table(encabezado_data, colWidths=[70*mm, 40*mm, 40*mm])
    encabezado_table.setStyle(TableStyle([
        ('SPAN', (0,0), (0,3)),  # Span de la columna "DE"
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (1,0), (1,-1), 'RIGHT')
    ]))
    
    # Tabla para el logo y el encabezado
    logo_encabezado_table = Table([[logo, encabezado_table]], colWidths=[50*mm, 130*mm])
    logo_encabezado_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (0, 0), 'RIGHT')
    ]))
    
    # Información de facturación y envío
    info_data = [
        ['FACTURAR A', 'ENVIAR A'],
        ['Leda Villareal', 'Leda Villareal'],
        ['Virgen Blanca 63', 'Cercas Bajas 68'],
        ['08759 Burgos, Burgos', '47300 Cádiz, Cádiz']
    ]
    info_table = Table(info_data, colWidths=[70*mm, 70*mm])
    info_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
    ]))
    
    # Detalles de los productos
    detalles_data = [
        ['CANT.', 'DESCRIPCIÓN', 'PRECIO UNITARIO', 'IMPORTE'],
        ['1', 'Talla pequeña traje de luces en rojo', '100.00', '100.00'],
        ['2', 'Mui grande churrolito', '25.00', '50.00'],
        ['3', 'Equipaje de Fútbol', '5.00', '15.00']
    ]
    detalles_table = Table(detalles_data, colWidths=[20*mm, 100*mm, 30*mm, 30*mm])
    detalles_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black)
    ]))
    
    # Subtotal e IVA
    total_data = [
        ['', 'Subtotal', '165.00'],
        ['', 'IVA 21.0%', '34.65']
    ]
    total_table = Table(total_data, colWidths=[120*mm, 30*mm, 30*mm])
    total_table.setStyle(TableStyle([
        ('ALIGN', (1,0), (-1,-1), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
    ]))
    
    # Total
    total_final_data = [['TOTAL', '199.65 €']]
    total_final_table = Table(total_final_data, colWidths=[150*mm, 30*mm])
    total_final_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black)
    ]))
    
    # Condiciones de pago
    condiciones = Paragraph('CONDICIONES Y FORMA DE PAGO<br/><br/>El pago se realizará en un plazo de 15 días<br/><br/>Banco Santander<br/>IBAN: ES12 3456 7891<br/>SWIFT/BIC: ABCDESM1XXX', styleN)
    
    # Firma
    firma = Paragraph('<br/><br/><br/><br/>Laura García', styleN)
    
    # Añadiendo elementos al documento
    elements.append(logo_encabezado_table)
    elements.append(Paragraph('<br/><br/>', styleN))
    elements.append(info_table)
    elements.append(Paragraph('<br/><br/>', styleN))
    elements.append(detalles_table)
    elements.append(Paragraph('<br/><br/>', styleN))
    elements.append(total_table)
    elements.append(Paragraph('<br/><br/>', styleN))
    elements.append(total_final_table)
    elements.append(Paragraph('<br/><br/>', styleN))
    elements.append(condiciones)
    elements.append(Paragraph('<br/><br/>', styleN))
    elements.append(firma)
    
    # Construcción del documento
    doc.build(elements)

# Uso de la función
create_invoice('/mnt/data/factura.pdf', '/mnt/data/logo.png')


# Función principal
if __name__ == "__main__":
    menu_principal()
