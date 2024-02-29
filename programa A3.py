import math

def rectangular_a_cilindricas(x, y, z):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta, z

def rectangular_a_esfericas(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.atan2(math.sqrt(x**2 + y**2), z)
    return r, theta, phi

# Coordenadas rectangulares
x = 3
y = 4
z = 5

# Conversión a coordenadas cilíndricas
r_cilindrica, theta_cilindrica, z_cilindrica = rectangular_a_cilindricas(x, y, z)
print("Coordenadas cilíndricas:")
print("r =", r_cilindrica)
print("theta =", theta_cilindrica)
print("z =", z_cilindrica)

# Conversión a coordenadas esféricas
r_esferica, theta_esferica, phi_esferica = rectangular_a_esfericas(x, y, z)
print("\nCoordenadas esféricas:")
print("r =", r_esferica)
print("theta =", theta_esferica)
print("phi =", phi_esferica)



