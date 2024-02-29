import numpy as np
import matplotlib.pyplot as plt

def transfer_function(coefficients, t):
    num = coefficients[0]
    den = [coefficients[1], coefficients[2], coefficients[3]]
    return np.polyval(num, t) / np.polyval(den, t)

def system_type(coefficients):
    discriminant = coefficients[1]**2 - 4 * coefficients[0] * coefficients[3]
    if discriminant > 0:
        return "Sobreamortiguado"
    elif discriminant == 0:
        return "Críticamente amortiguado"
    else:
        return "Subamortiguado"

def plot_response(coefficients):
    t = np.linspace(0, 20, 1000)
    response = transfer_function(coefficients, t)
    plt.plot(t, response)
    plt.title("Respuesta del sistema")
    plt.xlabel("Tiempo")
    plt.ylabel("Respuesta")
    plt.grid(True)
    plt.show()

def main():
    print("Ingrese los coeficientes de la función de transferencia de segundo orden:")
    a = float(input("Coeficiente a: "))
    b = float(input("Coeficiente b: "))
    c = float(input("Coeficiente c: "))
    
    coefficients = [1, b/a, c/a]
    
    print("\nTipo de sistema:", system_type(coefficients))
    
    plot_response(coefficients)

if __name__ == "__main__":
    main()
