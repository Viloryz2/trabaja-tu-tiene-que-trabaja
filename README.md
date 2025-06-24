

alumnos = []

def es_nombre_valido(nombre):
    return nombre.isalpha()

while True:
    print("\nMenú:")
    print("1. Agregar alumno")
    print("2. Mostrar todos los alumnos")
    print("3. Eliminar alumno")
    print("4. Cerrar")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        nombre = input("Ingresa el nombre del alumno: ")
        if es_nombre_valido(nombre):
            alumnos.append(nombre)
            print("Alumno agregado.")
        else:
            print("Nombre inválido. Solo se permiten letras.")
    elif opcion == "2":
        print("Lista de alumnos:")
        if alumnos:
            for alumno in alumnos:
                print(alumno)
        else:
            print("No hay alumnos registrados.")
    elif opcion == "3":
        nombre = input("Ingresa el nombre del alumno a eliminar: ")
        if nombre in alumnos:
            alumnos.remove(nombre)
            print("Alumno eliminado.")
        else:
            print("El alumno no está en la lista.")
    elif opcion == "4":
        print("Programa cerrado.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
