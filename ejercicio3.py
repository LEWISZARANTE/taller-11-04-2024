contactos = {}

# Función para registrar un contacto
def registrar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono del contacto: ")
    contactos[nombre] = telefono
    print("Contacto registrado con éxito.")

# Función para buscar un contacto
def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto que desea buscar: ")
    if nombre in contactos:
        telefono = contactos[nombre]
        print("El número de teléfono de", nombre, "es", telefono)
    else:
        print("No se encontró el contacto.")

# Menú principal
while True:
    print("\n==== Menú ====")
    print("1. Registrar contacto")
    print("2. Buscar contacto")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        registrar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

print("Gracias por usar el programa. ¡Hasta luego!")