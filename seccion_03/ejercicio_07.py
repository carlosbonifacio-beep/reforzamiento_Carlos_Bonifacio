# Ejercicio 07: Cálculos de un círculo

class Circulo:
    def __init__(self, radio):
        if isinstance(radio, (int, float)) and radio > 0:
            self.radio = radio
        else:
            self.radio = None
            print(f"Error: El radio '{radio}' no es válido. Debe ser mayor que cero.")

    def calcular_area(self):
        if self.radio is None:
            return "Cálculo no disponible por radio inválido"
        pi = 3.1416
        return pi * (self.radio ** 2)

    def calcular_perimetro(self):
        if self.radio is None:
            return "Cálculo no disponible por radio inválido"
        pi = 3.1416
        return 2 * pi * self.radio

# Tres objetos
c1 = Circulo(3)
c2 = Circulo(5)
c3 = Circulo(-2)

print("\nResultados del Círculo 1 (Radio: 3):")
print(f"Área: {c1.calcular_area()}")
print(f"Perímetro: {c1.calcular_perimetro()}")

print("\nResultados del Círculo 2 (Radio: 5):")
print(f"Área: {c2.calcular_area()}")
print(f"Perímetro: {c2.calcular_perimetro()}")

print("\nResultados del Círculo 3 (Radio: -2):")
print(f"Área: {c3.calcular_area()}")
print(f"Perímetro: {c3.calcular_perimetro()}")
