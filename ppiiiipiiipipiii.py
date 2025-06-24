alumnos = []

while True:
    print("\nMenú:")
    print("1. Agregar alumno")
    print("2. Mostrar todos los alumnos")
    print("3. Cerrar")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        nombre = input("Ingresa el nombre del alumno: ")
        alumnos.append(nombre)
        print("Alumno agregado.")
    elif opcion == "2":
        print("Lista de alumnos:")
        for alumno in alumnos:
            print(alumno)
        if not alumnos:
            print("No hay alumnos registrados.")
    elif opcion == "3":
        print("Programa cerrado.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
