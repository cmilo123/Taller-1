import math

def calcular_volumen_prisma(base, altura):
    return base * altura

def calcular_volumen_piramide(base, altura):
    return (1/3) * base * altura

def calcular_volumen_cono_truncado(radio1, radio2, altura):
    return math.pi * altura * (radio1**2 + radio2**2 + radio1*radio2) / 3

def calcular_volumen_cilindro(radio, altura):
    return math.pi * radio**2 * altura

def main():
    print("Bienvenido al programa de cálculo de volúmenes.")
    print("Seleccione el sólido geométrico para calcular su volumen:")
    print("1. Prisma")
    print("2. Pirámide")
    print("3. Cono truncado")
    print("4. Cilindro")

    opcion = int(input("Ingrese el número correspondiente a su selección: "))

    if opcion == 1:
        base = float(input("Ingrese la medida de la base del prisma: "))
        altura = float(input("Ingrese la altura del prisma: "))
        volumen = calcular_volumen_prisma(base, altura)
        print("El volumen del prisma es:", volumen)

    elif opcion == 2:
        base = float(input("Ingrese la medida de la base de la pirámide: "))
        altura = float(input("Ingrese la altura de la pirámide: "))
        volumen = calcular_volumen_piramide(base, altura)
        print("El volumen de la pirámide es:", volumen)

    elif opcion == 3:
        radio1 = float(input("Ingrese el radio mayor del cono truncado: "))
        radio2 = float(input("Ingrese el radio menor del cono truncado: "))
        altura = float(input("Ingrese la altura del cono truncado: "))
        volumen = calcular_volumen_cono_truncado(radio1, radio2, altura)
        print("El volumen del cono truncado es:", volumen)

    elif opcion == 4:
        radio = float(input("Ingrese el radio del cilindro: "))
        altura = float(input("Ingrese la altura del cilindro: "))
        volumen = calcular_volumen_cilindro(radio, altura)
        print("El volumen del cilindro es:", volumen)

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
