





def modificacion(tabla):
    limpiar_pantalla()
    conexion = conectar()
    cursor = conexion.cursor()

    if tabla == "1": 
        codigo_cliente = input("Ingrese el codigo de cliente a modificar: ")
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        nif_nie = input("Introduce tu Nif/Nie: ")
        direccion = input("Introduce tu dirección: ")
        cp= input("Introduce tu codigo postal: ")
        provincia = input("Introduce tu provinica: ")
        poblacion = input ("Introduce tu población: ")

        sql = "UPDATE cliente SET nombre = %s, apellido = %s, nif_nie = %s, direccion = %s, cp = %s, provincia = %s WHERE codigo_cliente = %s"
        valores = (nombre, apellido, nif_nie, direccion, cp, provincia, codigo_cliente, poblacion)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Cliente modificado exitosamente.")
    
    elif tabla == "2":
        codigo = input("Escriba un código postal: ")
        descripcion = input("Escriba una descripción: ")


        sql = "UPDATE codigopostal SET codigo = %s, descripcion = %s WHERE codigo = %s"
        valores = (codigo, descripcion)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Código postal modificado exitosamente.")
    
    elif tabla == "3":
        codigo = input("Escriba un código postal: ")
        descripcion = input("Escriba una descripción: ")

        sql = "UPDATE Poblaciones SET codigo = %s, descripcion = %s WHERE codigo = %s"
        valores = (codigo, descripcion)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Población modificada exitosamente.")
    
    elif tabla == "4":
        codigo= input("Escriba un código postal: ")
        descripcion = input("Escriba una descripción: ")

        sql = "UPDATE Provincias SET codigo = %s, descripcion = %s WHERE codigo = %s"
        valores = (codigo, descripcion)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Provincia modificada exitosamente.")
    
    elif tabla == "5":
        codigo_banco = input("Ingrese el ID del banco a modificar: ")
        nombre_entidad = input("Escriba el nombre de su banco: ")
        codigo_iban = input("Escriba el número de cuenta: ")
        codigo_swift = input("Escriba el código internacional: ")

        sql = "UPDATE Bancos SET nombre_entidad = %s, codigo_iban = %s, codigo_swift = %s WHERE codigo_banco = %s"
        valores = (nombre_entidad, codigo_iban, codigo_swift, codigo_banco)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Entidad modificada exitosamente.")
    
    elif tabla == "6":
        id_envio = input("Ingrese el ID de la dirección de envío a modificar: ")
        cp = input("Escriba el código postal de envío: ")
        poblacion = input("Escriba la población de envío: ")
        provincia = input("Escriba la provincia de envío: ")

        sql = "UPDATE direccionenvio SET codigo_postal = %s, poblacion = %s, provincia = %s WHERE id_envio = %s"
        valores = (cp, poblacion, provincia, id_envio)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Dirección de envío modificada exitosamente.")

    cursor.close()
    conexion.close()
    input("Presione Enter para continuar...")