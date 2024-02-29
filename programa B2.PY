import random

def generar_numeros_aleatorios():
    # Solicitar al usuario el rango
    minimo = int(input("Ingrese el valor mínimo del rango: "))
    maximo = int(input("Ingrese el valor máximo del rango: "))
    
    # Solicitar al usuario la cantidad de números aleatorios a generar
    cantidad = int(input("Ingrese la cantidad de números aleatorios a generar: "))

    # Generar y mostrar los números aleatorios
    print("Los números aleatorios en el rango [{}, {}] son:".format(minimo, maximo))
    for _ in range(cantidad):
        numero_aleatorio = random.randint(minimo, maximo)
        print(numero_aleatorio)

if __name__ == "__main__":
    generar_numeros_aleatorios()
