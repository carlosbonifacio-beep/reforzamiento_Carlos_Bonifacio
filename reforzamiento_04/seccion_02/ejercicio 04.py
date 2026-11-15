"""
Ejercicio 04. Sistema de préstamos para empleados
"""

class Persona:
    def __init__(self, nombre, edad, sueldo_mensual, meses_trabajados):
        self.nombre = nombre
        self.edad = edad
        self.sueldo_mensual = sueldo_mensual
        self.meses_trabajados = meses_trabajados

    def mostrar_datos(self):
        print(f"Empleado: {self.nombre} | Edad: {self.edad} años | Sueldo: S/. {self.sueldo_mensual:.2f} | Meses trabajados: {self.meses_trabajados}")

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def calcular_bonificacion(self):
        if self.es_mayor_de_edad():
            return self.sueldo_mensual * 0.20
        return 0.0

class PersonaPrestamo(Persona):
    def evaluar_prestamo(self):
        if self.edad > 25 and self.meses_trabajados > 12:
            prestamo = self.sueldo_mensual * 10
            print(f"Préstamo APROBADO: Puede acceder a un préstamo de S/. {prestamo:.2f}")
        else:
            print("Préstamo RECHAZADO: No cumple los requisitos (>25 años y >12 meses trabajados).")

emp1 = PersonaPrestamo("Carlos Mendoza", 30, 3500.0, 24)
emp2 = PersonaPrestamo("Ana Torres", 23, 2800.0, 18)
emp3 = PersonaPrestamo("Luis Gómez", 17, 1200.0, 6)

empleados = [emp1, emp2, emp3]

for emp in empleados:
    print("-" * 60)
    emp.mostrar_datos()
    print(f"Bonificación (20% si es mayor de edad): S/. {emp.calcular_bonificacion():.2f}")
    emp.evaluar_prestamo()