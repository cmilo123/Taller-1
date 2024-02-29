import numpy as np

def rotacion_x(angulo):
    """Realiza una rotación en el eje X.

    Args:
        angulo (float): Ángulo de rotación en radianes.

    Returns:
        numpy.ndarray: Matriz de rotación resultante.
    """
    matriz = np.array([[1, 0, 0],
                       [0, np.cos(angulo), -np.sin(angulo)],
                       [0, np.sin(angulo), np.cos(angulo)]])
    return matriz

def rotacion_y(angulo):
    """Realiza una rotación en el eje Y.

    Args:
        angulo (float): Ángulo de rotación en radianes.

    Returns:
        numpy.ndarray: Matriz de rotación resultante.
    """
    matriz = np.array([[np.cos(angulo), 0, np.sin(angulo)],
                       [0, 1, 0],
                       [-np.sin(angulo), 0, np.cos(angulo)]])
    return matriz

def rotacion_z(angulo):
    """Realiza una rotación en el eje Z.

    Args:
        angulo (float): Ángulo de rotación en radianes.

    Returns:
        numpy.ndarray: Matriz de rotación resultante.
    """
    matriz = np.array([[np.cos(angulo), -np.sin(angulo), 0],
                       [np.sin(angulo), np.cos(angulo), 0],
                       [0, 0, 1]])
    return matriz

# Ejemplo de uso:
angulo = np.pi/4  # Ángulo de 45 grados en radianes

# Rotación en el eje X
matriz_rotacion_x = rotacion_x(angulo)
print("Rotación en el eje X:")
print(matriz_rotacion_x)

# Rotación en el eje Y
matriz_rotacion_y = rotacion_y(angulo)
print("\nRotación en el eje Y:")
print(matriz_rotacion_y)

# Rotación en el eje Z
matriz_rotacion_z = rotacion_z(angulo)
print("\nRotación en el eje Z:")
print(matriz_rotacion_z)
