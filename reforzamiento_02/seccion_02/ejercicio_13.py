numeros = []

# Carga individual con append()
numeros.append(12)
numeros.append(19)
numeros.append(24)
numeros.append(31)
numeros.append(40)
numeros.append(45)
numeros.append(52)
numeros.append(63)
numeros.append(70)
numeros.append(81)

# Estadísticas
suma_total = sum(numeros)
promedio = suma_total / len(numeros)
mayor = max(numeros)
menor = min(numeros)

pares = sum(1 for n in numeros if n % 2 == 0)
impares = sum(1 for n in numeros if n % 2 != 0)

# Impresión
print(f"Números registrados: {numeros}")
print(f"Suma total: {suma_total}")
print(f"Promedio: {promedio:.2f}")
print(f"Número mayor: {mayor}")
print(f"Número menor: {menor}")
print(f"Cantidad de pares: {pares}")
print(f"Cantidad de impares: {impares}")