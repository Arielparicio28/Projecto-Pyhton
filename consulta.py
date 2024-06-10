def consulta(tabla):
    while True:
        mostrar_tablas()
        tabla = input("Seleccione una tabla: ")
        if tabla == "":
            print("\n--- Consulta de Clientes ---")
            conexion.execute("SELECT * FROM cliente")
            registros = conexion.fetchall()
            for registro in registros:
                print(f"ID: {registro[0]}, Nombre: {registro[1]}, Apellidos: {registro[2]}, Código Postal: {registro[3]}, Ciudad Facturación: {registro[4]}, Provincia Facturación: {registro[5]}, CIF/NIF: {registro[6]}")

        elif tabla == "":
            print("\n--- Consulta de Direcciones de Envío ---")
            conexion.execute("SELECT * FROM direccionenvio")
            registros = conexion.fetchall()
            for registro in registros:
                print(f"ID: {registro[0]}, Nombre: {registro[1]}, Apellidos: {registro[2]}, Código Postal: {registro[3]}, Ciudad Envío: {registro[4]}, Provincia Envío: {registro[5]}, CIF/NIF: {registro[6]}")

        elif tabla == "":
            print("\n--- Consulta de Entidades Financieras ---")
            conexion.execute("SELECT * FROM bancos ")
            registros = conexion.fetchall()
            for registro in registros:
                print(f"ID: {registro[0]}, Nombre del Banco: {registro[1]}, IBAN: {registro[2]}, SWIFT/BIC: {registro[3]}")

        elif tabla == "":
            print("Saliendo de la consulta de datos...")
            break
        else:
            print("Opción no válida, intente nuevamente.")