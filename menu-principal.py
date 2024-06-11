import mysql.connector
import os

# Función para conectar a la base de datos
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="datos"  # Especifica el nombre de tu base de datos aquí
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
            menu_facturacion()
        elif opcion == "3":
            menu_impresion_facturacion()
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
        print("2. Productos")
        print("3. Provincias")
        print("4. Entidades Bancarias")
        print("5. Códigos Postales")
        print("6. Direcciones de Envío")
        print("7. Empresas")
        print("8. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            submenu_tabla("Clientes")
        elif opcion == "2":
            submenu_tabla("Productos")
        elif opcion == "3":
            submenu_tabla("Provincias")
        elif opcion == "4":
            submenu_tabla("Entidades Bancarias")
        elif opcion == "5":
            submenu_tabla("Códigos Postales")
        elif opcion == "6":
            submenu_tabla("Direcciones de Envío")
        elif opcion == "7":
            submenu_tabla("Empresas")
        elif opcion == "8":
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