import sys
import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

ruta_conexion_bd = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "conexion"))
sys.path.append(ruta_conexion_bd)
from conexion_bd import obtener_conexion

ruta_factura = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "facturacion"))
sys.path.append(ruta_factura)
from facturacion import obtener_datos_empresa, obtener_datos_cliente


def obtener_datos_productos(nif):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
    SELECT p.descripcion, fp.cantidad, p.precio_unitario, (fp.cantidad * p.precio_unitario) AS total
    FROM cabecera fp
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
    float(total_general)
    return total_general,total_general * 1.21 # 21% IVA

def create_invoice(datos_cliente, productos, total_general, total_con_iva):
    datos_empresa = obtener_datos_empresa()
    fecha_factura = datetime.now().strftime("%d/%m/%Y")

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=20*mm, leftMargin=20*mm, topMargin=20*mm, bottomMargin=20*mm)
    elements = []
    styles = getSampleStyleSheet()
    styleN = styles['Normal']

    encabezado_data = [
        ['DE', 'N° DE FACTURA', 'ES-001'],
        [datos_empresa['Nombre-Empresa'], 'FECHA', fecha_factura],
        [datos_empresa['DirecciÓn'], 'N° DE PEDIDO', '1730/2019'],
        [f"{datos_empresa['Codigo-Postal']} {datos_empresa['Provincia']}", 'FECHA VENCIMIENTO', fecha_factura]
    ]
    encabezado_table = Table(encabezado_data, colWidths=[70*mm, 40*mm, 40*mm])
    encabezado_table.setStyle(TableStyle([
        ('SPAN', (0,0), (0,3)),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (1,0), (1,-1), 'RIGHT')
    ]))
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
    total_data = [
        ['', 'Subtotal', f"{total_general:.2f}"],
        ['', 'IVA 21.0%', f"{total_con_iva - total_general:.2f}"]
    ]
    total_table = Table(total_data, colWidths=[120*mm, 30*mm, 30*mm])
    total_table.setStyle(TableStyle([
        ('ALIGN', (1,0), (-1,-1), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
    ]))
    total_final_data = [['TOTAL', f"{total_con_iva:.2f} €"]]
    total_final_table = Table(total_final_data, colWidths=[150*mm, 30*mm])
    total_final_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black)
    ]))
    condiciones = Paragraph('CONDICIONES Y FORMA DE PAGO<br/><br/>El pago se realizará en un plazo de 15 días<br/><br/>Banco Santander<br/>IBAN: ES12 3456 7891<br/>SWIFT/BIC: ABCDESM1XXX', styleN)
    firma = Paragraph('<br/><br/><br/><br/>Laura García', styleN)
    elements.append(encabezado_table)
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
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

def guardar_factura_en_bd(nif_cliente, pdf):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO facturas (cliente_nif, fecha_factura, pdf) VALUES (%s, %s, %s)"
    fecha_factura = datetime.now().strftime("%Y-%m-%d")
    cursor.execute(sql, (nif_cliente, fecha_factura, pdf))
    conexion.commit()
    cursor.close()
    conexion.close()

def imprimir():
    nif_cliente = input("Introduce el NIF/NIE del cliente: ")
    try:
        datos_cliente = obtener_datos_cliente(nif_cliente)
    except ValueError as e:
        print(e)
        return
    productos = obtener_datos_productos(nif_cliente)
    if not productos:
        print("No se encontraron productos para este cliente.")
        return
    total_general, total_con_iva = calcular_total_general(productos)
    pdf = create_invoice(datos_cliente, productos, total_general, total_con_iva)
    guardar_factura_en_bd(nif_cliente, pdf)
    print("\nFactura generada y guardada en la base de datos.")
    
     # Generar el PDF
    pdf_content = create_invoice(obtener_datos_empresa, datos_cliente, productos, total_general, total_con_iva)
 
   # create_invoice('factura.pdf', 'logo.png', datos_cliente, productos, total_general, total_con_iva)

# Ejecutar la función para generar la factura

    # Guardar el PDF en la base de datos
    guardar_factura_en_bd(nif_cliente, pdf_content)
    print("\nFactura generada y guardada en la base de datos.")

if __name__ == '__main__':
    imprimir()
