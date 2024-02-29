class CilindroNeumatico:
    def __init__(self, diametro_piston, diametro_barra, presion):
        self.diametro_piston = diametro_piston
        self.diametro_barra = diametro_barra
        self.presion = presion

    def calcular_fuerza_avance(self):
        area_piston = (3.14159 * (self.diametro_piston / 2) ** 2)
        fuerza_avance = area_piston * self.presion
        return fuerza_avance

    def calcular_fuerza_retroceso(self):
        area_barra = (3.14159 * (self.diametro_barra / 2) ** 2)
        fuerza_retroceso = area_barra * self.presion
        return fuerza_retroceso

# Valores predefinidos para el cilindro neumático
diametro_piston = 10  # en unidades de longitud
diametro_barra = 5  # en unidades de longitud
presion = 100  # en unidades de presión (por ejemplo, PSI)

# Crear una instancia del cilindro neumático con los valores predefinidos
cilindro = CilindroNeumatico(diametro_piston, diametro_barra, presion)

# Calcular fuerza de avance y retroceso
fuerza_avance = cilindro.calcular_fuerza_avance()
fuerza_retroceso = cilindro.calcular_fuerza_retroceso()

# Imprimir los resultados
print("Fuerza de avance:", fuerza_avance)
print("Fuerza de retroceso:", fuerza_retroceso)
