from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet

import sys
import os


ruta_conexion_bd = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","conexion"))
sys.path.append(ruta_conexion_bd)
from conexion_bd import obtener_conexion

def obtener_datos_empresa():
    return {
        "nombre": "Nombre de la Empresa",
        "cif_nie": "CIF_NIE de la Empresa",
        "direccion": "Dirección de la Empresa",
        "codigo_postal": "Código Postal de la Empresa",
        "provincia": "Provincia de la Empresa"
    }

def obtener_datos_cliente(nif):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "SELECT nombre, apellido, direccion, cp, provincia FROM cliente WHERE nif_nie = %s"
    cursor.execute(sql, (nif,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()
    if resultado and len(resultado) == 5:
        return {
            "nombre": resultado[0],
            "apellido": resultado[1],
            "direccion": resultado[2],
            "codigo_postal": resultado[3],
            "provincia": resultado[4]
        }
    else:
        raise ValueError("No se encontraron datos suficientes para el cliente con NIF/NIE proporcionado.")

def obtener_datos_productos(nif):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
    SELECT c.nombre, fp.cantidad, p.precio_unitario, (fp.cantidad * p.precio_unitario) AS total
    FROM factura fp
    JOIN productos p ON fp.codigo_producto = p.id
    JOIN factura f ON fp.id_factura = f.id
    JOIN cliente c ON f.codigo_cliente = c.id
    WHERE c.nif_nie = %s
    """
    cursor.execute(sql, (nif,))
    productos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return [{"producto": row[0], "cantidad": row[1], "precio_unitario": row[2], "total": row[3]} for row in productos]

def calcular_total_general(productos):
    total_general = sum(producto['total'] for producto in productos)
    return total_general, total_general * 1.21  # 21% IVA

def create_invoice(pdf_path, logo_path, datos_cliente, productos, total_general, total_con_iva):
    datos_empresa = obtener_datos_empresa()
    fecha_factura = datetime.now().strftime("%d/%m/%Y")

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
        [datos_empresa['nombre'], 'FECHA', fecha_factura],
        [datos_empresa['direccion'], 'N° DE PEDIDO', '1730/2019'],
        [f"{datos_empresa['codigo_postal']} {datos_empresa['provincia']}", 'FECHA VENCIMIENTO', fecha_factura]
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
        [f"{datos_cliente['nombre']} {datos_cliente['apellido']}", f"{datos_cliente['nombre']} {datos_cliente['apellido']}"],
        [datos_cliente['direccion'], datos_cliente['direccion']],
        [f"{datos_cliente['codigo_postal']} {datos_cliente['provincia']}", f"{datos_cliente['codigo_postal']} {datos_cliente['provincia']}"]
    ]
    info_table = Table(info_data, colWidths=[70*mm, 70*mm])
    info_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
    ]))
    # Detalles de los productos
    detalles_data = [['CANT.', 'DESCRIPCIÓN', 'PRECIO UNITARIO', 'IMPORTE']]
    for producto in productos:
        detalles_data.append([
            producto['cantidad'],
            producto['producto'],
            f"{producto['precio_unitario']:.2f}",
            f"{producto['total']:.2f}"
        ])
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
        ['', 'Subtotal', f"{total_general:.2f}"],
        ['', 'IVA 21.0%', f"{total_con_iva - total_general:.2f}"]
    ]
    total_table = Table(total_data, colWidths=[120*mm, 30*mm, 30*mm])
    total_table.setStyle(TableStyle([
        ('ALIGN', (1,0), (-1,-1), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
    ]))
    # Total
    total_final_data = [['TOTAL', f"{total_con_iva:.2f} €"]]
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
 
def imprimir():
    obtener_datos_empresa()
    nif_cliente = input("Introduce el NIF/NIE del cliente: ")
    try:
        datos_cliente = obtener_datos_cliente(nif_cliente)
    except ValueError as e:
        print(e)
        return
    productos = obtener_datos_productos(nif_cliente)
    total_general, total_con_iva = calcular_total_general(productos)
 
    create_invoice('/mnt/data/factura.pdf', '/mnt/data/logo.png', datos_cliente, productos, total_general, total_con_iva)

# Ejecutar la función para generar la factura


