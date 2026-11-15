"""
Ejercicio 06. Cálculo de bonificaciones según el tipo de empleado
"""

class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base
        self.modalidad = "General"

    def calcular_sueldo_final(self):
        return self.sueldo_base

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} | Modalidad: {self.modalidad} | Sueldo Base: S/. {self.sueldo_base:.2f} | Sueldo Final: S/. {self.calcular_sueldo_final():.2f}")

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, sueldo_base):
        super().__init__(nombre, sueldo_base)
        self.modalidad = "Tiempo Completo"

    def calcular_sueldo_final(self):
        return self.sueldo_base * 1.15

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, sueldo_base):
        super().__init__(nombre, sueldo_base)
        self.modalidad = "Medio Tiempo"

    def calcular_sueldo_final(self):
        return self.sueldo_base * 1.05

tc1 = EmpleadoTiempoCompleto("Sofía Paredes", 4000.0)
tc2 = EmpleadoTiempoCompleto("Jorge Chávez", 3200.0)
mt1 = EmpleadoMedioTiempo("Valeria Quispe", 1500.0)
mt2 = EmpleadoMedioTiempo("Diego Rojas", 1800.0)

for emp in [tc1, tc2, mt1, mt2]:
    emp.mostrar_datos()