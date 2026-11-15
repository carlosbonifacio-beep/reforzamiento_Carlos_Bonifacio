"""
Ejercicio 05. Sistema de figuras geométricas
"""

PI = 3.1416

class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(f"Figura: {self.nombre}")

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        if not (isinstance(base, (int, float)) and isinstance(altura, (int, float))) or base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser valores numéricos mayores que cero.")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def mostrar_info(self):
        self.mostrar_nombre()
        print(f"Dimensiones -> Base: {self.base:.2f}, Altura: {self.altura:.2f}")
        print(f"Área: {self.calcular_area():.2f} | Perímetro: {self.calcular_perimetro():.2f}\n")

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        if not isinstance(radio, (int, float)) or radio <= 0:
            raise ValueError("El radio debe ser un valor numérico mayor que cero.")
        self.radio = radio

    def calcular_area(self):
        return PI * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * PI * self.radio

    def mostrar_info(self):
        self.mostrar_nombre()
        print(f"Dimensiones -> Radio: {self.radio:.2f}")
        print(f"Área: {self.calcular_area():.2f} | Perímetro: {self.calcular_perimetro():.2f}\n")

try:
    rect1 = Rectangulo(5, 3)
    rect2 = Rectangulo(10.5, 4.2)
    circ1 = Circulo(4)
    circ2 = Circulo(7.5)

    for figura in [rect1, rect2, circ1, circ2]:
        figura.mostrar_info()
except ValueError as e:
    print(f"Error de validación: {e}")