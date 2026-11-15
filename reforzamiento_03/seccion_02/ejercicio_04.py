# Ejercicio 04: Suma de dígitos y comparación

def sumar_digitos(numero):
    suma = 0
    for digito in str(abs(numero)):
        suma += int(digito)
    return suma

num_1 = 583
num_2 = 241

suma_1 = sumar_digitos(num_1)
suma_2 = sumar_digitos(num_2)

print(f"Suma de dígitos de {num_1}: {suma_1}")
print(f"Suma de dígitos de {num_2}: {suma_2}")

if suma_1 > suma_2:
    print(f"El número {num_1} tiene mayor suma de dígitos.")
elif suma_2 > suma_1:
    print(f"El número {num_2} tiene mayor suma de dígitos.")
else:
    print("Existe un empate en la suma de dígitos.")

menores_a_10 = []
if suma_1 < 10:
    menores_a_10.append(num_1)
if suma_2 < 10:
    menores_a_10.append(num_2)

print(f"Números con suma de dígitos menor que 10: {menores_a_10 if menores_a_10 else 'Ninguno'}")