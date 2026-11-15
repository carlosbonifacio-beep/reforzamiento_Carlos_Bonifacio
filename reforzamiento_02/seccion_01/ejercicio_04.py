# 5 calificaciones
nota1 = 14.5
nota2 = 18.0
nota3 = 11.5
nota4 = 16.0
nota5 = 15

#suma de las notas y promedio
Suma_notas = (nota1 + nota2 + nota3 + nota4 + nota5)
promedio = Suma_notas / 5

#diferencia entre nota alta y baja
Nota_mayor = max(nota1, nota2, nota3, nota4, nota5)
Nota_menor = min(nota1, nota2, nota3, nota4, nota5)
Diferencia = Nota_mayor - Nota_menor

#condicion de aprobacion
if promedio >= 11:
    estado = "APROVADO"
else:
    estado = "DESAPROBADO"

#Resultados
print(f"Notas: {nota1}, {nota2}, {nota3}, {nota4}, {nota5}")
print(f"Suma de notas: {Suma_notas:.2f}")
print(f"Promedio de notas: {promedio:.2f}")
print(f"Diferencia entre nota mayor y menor: {Diferencia:.2f}")
print(f"Estado: {estado}")
