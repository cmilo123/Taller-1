import numpy as np
import matplotlib.pyplot as plt

# Función para convertir temperatura a resistencia para un sensor PT100
def temperatura_a_resistencia(temperatura):
    # Coeficientes para la ecuación de conversión
    A = 3.9083e-3
    B = -5.775e-7
    R0 = 100  # Resistencia a 0°C
    
    # Convertir temperatura a resistencia
    R = R0 * (1 + A*temperatura + B*temperatura**2)
    return R

# Generar datos de temperatura desde -200°C a 200°C
temperaturas = np.linspace(-200, 200, 1000)

# Obtener resistencias correspondientes a las temperaturas
resistencias = temperatura_a_resistencia(temperaturas)

# Graficar temperatura vs resistencia
plt.figure(figsize=(10, 6))
plt.plot(temperaturas, resistencias, color='blue')
plt.title('Comportamiento del sensor PT100')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ohm)')
plt.grid(True)
plt.show()
