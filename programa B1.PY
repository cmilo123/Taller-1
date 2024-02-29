def calcular_potencia(corriente, voltaje):
    potencia = corriente * voltaje
    return potencia

def main():
    corriente = float(input("Ingrese el valor de corriente (en amperios): "))
    voltaje = float(input("Ingrese el valor de voltaje (en voltios): "))
    
    potencia = calcular_potencia(corriente, voltaje)
    
    print("La potencia consumida por el circuito es:", potencia, "vatios")

if __name__ == "__main__":
    main()
