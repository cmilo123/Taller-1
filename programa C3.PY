import numpy as np
import matplotlib.pyplot as plt

def carga_descarga_RC(V, R, C, t):
    """
    Calcula el voltaje a través de un circuito RC en función del tiempo
    """
    tau = R * C  # Constante de tiempo
    carga = V * (1 - np.exp(-t/tau))  # Carga
    descarga = V * np.exp(-t/tau)  # Descarga
    return carga, descarga

def graficar_carga_descarga(V, R, C):
    """
    Grafica la carga y descarga de un circuito RC
    """
    t = np.linspace(0, 5*R*C, 1000)  # Tiempo de 0 a 5 veces la constante de tiempo
    carga, descarga = carga_descarga_RC(V, R, C, t)
    
    plt.plot(t, carga, label='Carga')
    plt.plot(t, descarga, label='Descarga')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (V)')
    plt.title('Carga y Descarga de un Circuito RC')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    V = float(input("Ingrese el valor de voltaje (V): "))
    R = float(input("Ingrese el valor de resistencia (Ω): "))
    C = float(input("Ingrese el valor de capacitancia (μF): "))
    
    graficar_carga_descarga(V, R, C)
