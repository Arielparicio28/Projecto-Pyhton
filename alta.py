def alta(tabla):
    limpiar_pantalla()
    conexion = conectar()
    cursor = conexion.cursor()
 
 #Tabla Clientes

    if tabla == "Clientes":
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        nif = input("Introduce tu Nif/Nie ")
        direccion = input("Introduce tu dirección")
        codigoPostal = input("Introduce tu codigo postal")
        provincia = input("Introduce tu provinica")
       
 
        sql = "INSERT INTO cliente (nombre, apellido, nif_nie, direccion, codigopostal, provincia) VALUES (%s, %s,%s,%s,%s,%s)"
        valores = (nombre, apellido, nif, direccion, codigoPostal, provincia)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Cliente agregado exitosamente.")
    
    #Tabla codigo postal

    elif tabla == "":
        codigo = input("Escriba un código postal: ")
        descripcion = input("Escriba una descripción: ")
      
        sql = "INSERT INTO codigopostal (codigo, descripcion) VALUES (%s, %s)"
        val = (codigo, descripcion)
        conexion.execute(sql, val)
        conexion.commit()
        print("Datos introducidos correctamente.")
    
#Tabla poblacion

    elif tabla == "":
        codigoP = input("Escriba un código postal: ")
        descripcionP = input("Escriba una descripción: ")
      
        sql = "INSERT INTO poblacion (codigo, descripcion) VALUES (%s, %s)"
        val = (codigoP, descripcionP)
        conexion.execute(sql, val)
        conexion.commit()
        print("Datos introducidos correctamente.")

#Tabla Provincias

    elif tabla == "":
        codigoPro = input("Escriba un código postal: ")
        descripcionPro = input("Escriba una descripción: ")
      
        sql = "INSERT INTO provincias (codigo, descripcion) VALUES (%s, %s)"
        val = (codigoPro, descripcionPro)
        conexion.execute(sql, val)
        conexion.commit()
        print("Datos introducidos correctamente.")
    
#Tabla Banco

    elif tabla == "":
            
            nombreBanco = input("Escriba el nombre de su banco: ")
            iban = input("Escriba el número de cuenta: ")
            swift = input("Escriba el código internacional: ")

            sql = "INSERT INTO nombre_entidad_financiera (nombre_entidad, codigo_iban, codigo_swift) VALUES (%s, %s, %s)"
            val = (nombreBanco, iban, swift)
            conexion.execute(sql, val)
            conexion.commit()
            print("Datos introducidos correctamente.")

#Tabla dirección envio

    elif tabla == "":
            
            codigoPosenvio = input("Escriba el codigo de envio ")
            poblacionenvio = input("Escriba la poblacion de envio: ")
            provinciaenvio = input("Escriba la provincia de envio: ")

            sql = "INSERT INTO direccionenvio (codigo_postal, poblacion, provincia) VALUES (%s, %s, %s)"
            val = (codigoPosenvio, poblacionenvio, provinciaenvio )
            conexion.execute(sql, val)
            conexion.commit()
            print("Datos introducidos correctamente.")


    cursor.close()
    conexion.close()
    input("Presione Enter para continuar...")

 

 