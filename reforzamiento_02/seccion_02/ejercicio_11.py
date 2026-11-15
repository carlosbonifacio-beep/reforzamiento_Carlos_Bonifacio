estudiantes = []
cantidad_estudiantes = 4

est1, est2, est3, est4 = "Lucía", "Jorge", "Mateo", "Sofía"

# Append()
estudiantes.append(est1)
estudiantes.append(est2)
estudiantes.append(est3)
estudiantes.append(est4)

# Verificaciones
total_registrados = len(estudiantes)
coincide = "Sí" if total_registrados == cantidad_estudiantes else "No"

# Mostrar resultados
print(f"Cantidad de estudiantes prevista: {cantidad_estudiantes}")
print(f"Estudiantes registrados: {estudiantes}")
print(f"Total de estudiantes registrados: {total_registrados}")
print(f"¿Coincide con la cantidad prevista?: {coincide}")
print(f"Primer estudiante: {estudiantes[0]}")
print(f"Último estudiante: {estudiantes[-1]}")
print(f"Orden inverso: {estudiantes[::-1]}")
