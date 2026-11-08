# Ejercicio 02: Registro de calificaciones

notas = {"Ana": 16, "Luis": 10, "María": 18, "Pedro": 8, "Rosa": 14}

print("Estudiantes registrados:")
for estudiante, nota in notas.items():
    print(f"{estudiante}: {nota}")

aprobados = [estudiante for estudiante, nota in notas.items() if nota >= 11]
print("Estudiantes aprobados:", ", ".join(aprobados))

suma_notas = sum(notas.values())
promedio = suma_notas / len(notas)
print(f"Promedio general: {promedio:.2f}")

max_nota = -1
estudiante_max = ""
for estudiante, nota in notas.items():
    if nota > max_nota:
        max_nota = nota
        estudiante_max = estudiante

print(f"Nota más alta: {max_nota} ({estudiante_max})")

desaprobados = sum(1 for nota in notas.values() if nota < 11)
print(f"Estudiantes desaprobados: {desaprobados}")
