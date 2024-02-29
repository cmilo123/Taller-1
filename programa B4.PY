def main():
    print("Bienvenido al programa de selección de robots.")
    print("Por favor, elija el tipo de robot:")
    print("1. Robot Cilíndrico")
    print("2. Robot Cartesiano")
    print("3. Robot Esférico")

    opcion = input("Ingrese el número correspondiente a su elección: ")

    if opcion == "1":
        print("Ha seleccionado un Robot Cilíndrico.")
        print("Tiene 2 articulaciones.")
    elif opcion == "2":
        print("Ha seleccionado un Robot Cartesiano.")
        print("Tiene 3 articulaciones.")
    elif opcion == "3":
        print("Ha seleccionado un Robot Esférico.")
        print("Tiene 2 articulaciones.")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1, 2 o 3).")

if __name__ == "__main__":
    main()
