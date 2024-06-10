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
       
 
        sql = "INSERT INTO cliente (nombre, apellido, nif_nie, direccion, codigopostal) VALUES (%s, %s,%s,%s,%s,%s)"
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



    elif tabla == "4":
            print("\n--- Alta de Producto ---")
            descripcionProducto = input("Escriba la descripción del producto: ")
            cantidad = input("Introduzca la cantidad a comprar: ")

            sql = "INSERT INTO productos (Cantidad, Descripcion) VALUES (%s, %s)"
            val = (cantidad, descripcionProducto)
            conexion.execute(sql, val)
            conexion.commit()
            print("Dato introducido correctamente.")
 

    cursor.close()
    conexion.close()
    input("Presione Enter para continuar...")

 

 