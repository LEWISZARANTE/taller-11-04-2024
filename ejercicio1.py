estudiantes = []

def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    carrera = input("Ingrese la carrera del estudiante: ")
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }
    estudiantes.append(estudiante)
    print("Información del estudiante registrada con éxito.")


def buscar_estudiante():
    nombre = input("Ingrese el nombre del estudiante que desea buscar: ")
    encontrado = False
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            print("Nombre:", estudiante["nombre"])
            print("Edad:", estudiante["edad"])
            print("Carrera:", estudiante["carrera"])
            encontrado = True
            break
    if not encontrado:
        print("No se encontró al estudiante en la lista.")


while True:
    print("\n==== Menú ====")
    print("1. Registrar estudiante")
    print("2. Buscar estudiante")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        registrar_estudiante()
    elif opcion == "2":
        buscar_estudiante()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

print("Gracias por usar el programa. ¡Hasta luego!")