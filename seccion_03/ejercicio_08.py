# Ejercicio 08: Registro de alumnos

class Alumno:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def mostrar_datos(self):
        print(f"Alumno: {self.nombre} | Edad: {self.edad} | Nota Final: {self.nota_final} | Condición: {self.condicion_academica()}")

    def condicion_academica(self):
        if self.nota_final >= 11:
            return "Aprobado"
        else:
            return "Desaprobado"

# Tres objetos
alumno1 = Alumno("Ana", 18, 16)
alumno2 = Alumno("Luis", 20, 9)
alumno3 = Alumno("Rosa", 19, 13)

# Almacen
grupo_alumnos = [alumno1, alumno2, alumno3]

print("Listado general de alumnos:")
for alumno in grupo_alumnos:
    alumno.mostrar_datos()
