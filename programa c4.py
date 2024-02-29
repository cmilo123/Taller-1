import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def dibujar_vector(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Dibujar el sistema de coordenadas
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='X')
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', label='Y')
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', label='Z')

    # Dibujar el vector ingresado por el usuario
    ax.quiver(0, 0, 0, x, y, z, color='k', label='Vector')

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

    plt.show()

def main():
    # Solicitar al usuario las coordenadas del vector
    x = float(input("Ingrese la coordenada X del vector: "))
    y = float(input("Ingrese la coordenada Y del vector: "))
    z = float(input("Ingrese la coordenada Z del vector: "))

    # Dibujar el vector
    dibujar_vector(x, y, z)

if __name__ == "__main__":
    main()
