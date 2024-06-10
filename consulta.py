def consultas(tabla):
    limpiar_pantalla()
    conexion = conectar()
    cursor = conexion.cursor()
 
    # Tabla Clientes
    if tabla == "Clientes":
        nif = input("Introduce tu Nif/Nie: ")
        sql = "SELECT * FROM cliente WHERE nif_nie = %s"
        cursor.execute(sql, (nif,))
        resultado = cursor.fetchall()
        for cliente in resultado:
            print(f"Nombre: {cliente[1]}, Apellido: {cliente[2]}, Dirección: {cliente[4]}, Código Postal: {cliente[5]}, Provincia: {cliente[6]}")
    
    # Tabla Código Postal
    elif tabla == "CodigoPostal":
        codigo = input("Escriba un código postal: ")
        sql = "SELECT * FROM codigopostal WHERE codigo = %s"
        cursor.execute(sql, (codigo,))
        resultado = cursor.fetchall()
        for codigopostal in resultado:
            print(f"Código: {codigopostal[1]}, Descripción: {codigopostal[2]}")
    
    # Tabla Población
    elif tabla == "Poblacion":
        codigoP = input("Escriba un código postal: ")
        sql = "SELECT * FROM poblacion WHERE codigo = %s"
        cursor.execute(sql, (codigoP,))
        resultado = cursor.fetchall()
        for poblacion in resultado:
            print(f"Código: {poblacion[1]}, Descripción: {poblacion[2]}")

    # Tabla Provincias
    elif tabla == "Provincias":
        codigoPro = input("Escriba un código postal: ")
        sql = "SELECT * FROM provincias WHERE codigo = %s"
        cursor.execute(sql, (codigoPro,))
        resultado = cursor.fetchall()
        for provincia in resultado:
            print(f"Código: {provincia[1]}, Descripción: {provincia[2]}")
    
    # Tabla Banco
    elif tabla == "Banco":
        nombreBanco = input("Escriba el nombre de su banco: ")
        sql = "SELECT * FROM bancos WHERE nombre_entidad = %s"
        cursor.execute(sql, (nombreBanco,))
        resultado = cursor.fetchall()
        for banco in resultado:
            print(f"Nombre del Banco: {banco[1]}, IBAN: {banco[2]}, SWIFT: {banco[3]}")

    # Tabla Dirección Envío
    elif tabla == "DireccionEnvio":
        codigoPosenvio = input("Escriba el código de envío: ")
        sql = "SELECT * FROM direccionenvio WHERE codigo_postal = %s"
        cursor.execute(sql, (codigoPosenvio,))
        resultado = cursor.fetchall()
        for direccion in resultado:
            print(f"Código Postal: {direccion[1]}, Población: {direccion[2]}, Provincia: {direccion[3]}")

    cursor.close()
    conexion.close()
    input("Presione Enter para continuar...")
