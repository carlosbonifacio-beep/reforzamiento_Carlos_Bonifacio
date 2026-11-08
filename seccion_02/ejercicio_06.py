# Ejercicio 06: Análisis de ventas semanales

def calcular_total(ventas):
    return sum(ventas)

def calcular_promedio(ventas):
    return sum(ventas) / len(ventas) if len(ventas) > 0 else 0

def calcular_maximo(ventas):
    return max(ventas) if ventas else 0

def contar_superiores_promedio(ventas):
    promedio = calcular_promedio(ventas)
    return sum(1 for v in ventas if v > promedio)

ventas = [150, 220, 180, 300, 175, 260, 190]

total = calcular_total(ventas)
promedio = calcular_promedio(ventas)
maximo = calcular_maximo(ventas)
superiores = contar_superiores_promedio(ventas)

print("Ventas semanales:", ventas)
print(f"1. Total vendido en la semana: {total} (Suma acumulada de los 7 días)")
print(f"2. Promedio diario de ventas: {promedio:.2f} (Venta media por día)")
print(f"3. Venta máxima: {maximo} (Día con mayores ingresos)")
print(f"4. Días que superaron el promedio: {superiores} (Días por encima de la media)")