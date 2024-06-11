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
