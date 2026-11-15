#administracion de estudiantes
estudiantes = ["Ana", "Pedro", "Luis", "María", "Carlos"]
print(f"Lista original: {estudiantes}")

buscado = "Luis"
nuevo_estudiante = "Rosa"

# Búsqueda y modificación
if buscado in estudiantes:
    estudiantes.remove(buscado)
    print(f"Estudiante buscado: {buscado}")
    print("Resultado: Estudiante eliminado correctamente.")
else:
    print(f"Estudiante '{buscado}' no encontrado. Agregándolo a la lista...")
    estudiantes.append(buscado)

# Insertar en la segunda posición (índice 1)
estudiantes.insert(1, nuevo_estudiante)
print(f"Nuevo estudiante insertado: {nuevo_estudiante}")
print(f"Lista actualizada: {estudiantes}")
print(f"Cantidad de estudiantes: {len(estudiantes)}")