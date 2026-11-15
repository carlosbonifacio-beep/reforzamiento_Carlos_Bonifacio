#conversion numerica y verificacion de multiplos
valor_1 = 50.8
valor_2 = 6.4

# Conversion a enteros
int1 = int(valor_1)
int2 = int(valor_2)

# Verificación de múltiplo
if int2 != 0:
    es_multiplo = "Sí" if (int1 % int2 == 0) else "No"
    residuo = int1 % int2
    cociente = int1 / int2
else:
    es_multiplo = "No se puede evaluar (división entre 0)"
    residuo = 0
    cociente = 0.0

# Salida
print(f"Primer valor decimal: {valor_1}")
print(f"Segundo valor decimal: {valor_2}")
print(f"Primer entero: {int1}")
print(f"Segundo entero: {int2}")
print(f"¿El primer número es múltiplo del segundo?: {es_multiplo}")
print(f"Residuo: {residuo}")
print(f"Cociente: {cociente:.2f}")