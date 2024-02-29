import math

def rtd_resistencia(temperatura):
    # Coeficientes de la ecuación de Callendar-Van Dusen
    A = 3.9083e-3
    B = -5.775e-7
    R0 = 100.0  # Resistencia a 0°C
    
    # Convertir temperatura a kelvin
    temperatura_kelvin = temperatura + 273.15
    
    # Calcular resistencia
    resistencia = R0 * (1 + A * temperatura_kelvin + B * temperatura_kelvin**2)
    return resistencia

# Definir una lista de temperaturas en grados Celsius
temperaturas = [0, 10, 20, 30, 40]

# Calcular y mostrar la resistencia para cada temperatura
for temp in temperaturas:
    resistencia = rtd_resistencia(temp)
    print(f"A {temp}°C, la resistencia de la RTD es {resistencia:.2f} ohms.")
