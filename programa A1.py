import numpy as np

def suma_vectores(v1, v2):
    return v1 + v2

def resta_vectores(v1, v2):
    return v1 - v2

def producto_punto(v1, v2):
    return np.dot(v1, v2)

def producto_cruz(v1, v2):
    return np.cross(v1, v2)

def division_vectores(v1, v2):
    return v1 / v2

# Vectores previamente inicializados
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Operaciones
resultado_suma = suma_vectores(vector1, vector2)
resultado_resta = resta_vectores(vector1, vector2)
resultado_producto_punto = producto_punto(vector1, vector2)
resultado_producto_cruz = producto_cruz(vector1, vector2)
resultado_division = division_vectores(vector1, vector2)

print("Resultado de la suma:", resultado_suma)
print("Resultado de la resta:", resultado_resta)
print("Resultado del producto punto:", resultado_producto_punto)
print("Resultado del producto cruz:", resultado_producto_cruz)
print("Resultado de la división:", resultado_division)



