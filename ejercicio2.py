inventario = {}

# Función para agregar un producto al inventario
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad disponible del producto: "))
    inventario[nombre] = cantidad
    print("Producto agregado al inventario con éxito.")

# Función para buscar un producto en el inventario
def buscar_producto():
    nombre = input("Ingrese el nombre del producto que desea buscar: ")
    if nombre in inventario:
        cantidad = inventario[nombre]
        print("Hay", cantidad, "unidades disponibles del producto", nombre)
    else:
        print("El producto no se encuentra en el inventario.")

# Menú principal
while True:
    print("\n==== Menú ====")
    print("1. Agregar producto al inventario")
    print("2. Buscar producto en el inventario")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        buscar_producto()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

print("Gracias por usar el programa. ¡Hasta luego!")