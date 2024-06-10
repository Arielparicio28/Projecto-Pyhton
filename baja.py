def baja(tabla):
    limpiar_pantalla()
    conexion = conectar()
    cursor = conexion.cursor()
 
    # Tabla Clientes
    if tabla == "Clientes":
        nif = input("Introduce el Nif/Nie del cliente a eliminar: ")
        sql = "DELETE FROM cliente WHERE nif_nie = %s"
        valores = (nif,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Cliente eliminado exitosamente.")
    
    # Tabla código postal
    elif tabla == "CodigoPostal":
        codigo = input("Escriba el código postal a eliminar: ")
        sql = "DELETE FROM codigopostal WHERE codigo = %s"
        valores = (codigo,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Código postal eliminado correctamente.")
    
    # Tabla población
    elif tabla == "Poblacion":
        codigoP = input("Escriba el código postal de la población a eliminar: ")
        sql = "DELETE FROM poblacion WHERE codigo = %s"
        valores = (codigoP,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Población eliminada correctamente.")

    # Tabla provincias
    elif tabla == "Provincias":
        codigoPro = input("Escriba el código postal de la provincia a eliminar: ")
        sql = "DELETE FROM provincias WHERE codigo = %s"
        valores = (codigoPro,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Provincia eliminada correctamente.")
    
    # Tabla banco
    elif tabla == "Banco":
        iban = input("Escriba el número de cuenta (IBAN) del banco a eliminar: ")
        sql = "DELETE FROM nombre_entidad_financiera WHERE codigo_iban = %s"
        valores = (iban,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Banco eliminado correctamente.")

    # Tabla dirección de envío
    elif tabla == "DireccionEnvio":
        codigoPosenvio = input("Escriba el código postal de envío a eliminar: ")
        sql = "DELETE FROM direccionenvio WHERE codigo_postal = %s"
        valores = (codigoPosenvio,)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Dirección de envío eliminada correctamente.")

    cursor.close()
    conexion.close()
    input("Presione Enter para continuar...")
