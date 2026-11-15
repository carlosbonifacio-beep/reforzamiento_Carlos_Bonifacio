#Conversion de temperaturas
#temperaturas
Temperatura1_C = 28.5
Temperatura2_C = 12.0

#Conversion de la temperatura 1
f1 = (Temperatura1_C * 9 / 5) +32
K1 = Temperatura1_C + 273.15

#Conversion de la temperatura 2
f2 = (Temperatura2_C * 9 / 5) +32
k2 = Temperatura2_C + 273.15

#diferencia
Diferencia = abs(Temperatura1_C - Temperatura2_C)

#resultados
print(f"Temperatura 1: {Temperatura1_C:.1f}°C")
print(f"Fahrenheit: {f1:.2f}°F")
print(f"Kelvin: {K1:.2f} K\n")

print(f"Temperatura 2: {Temperatura2_C:.1f}°C")
print(f"Fahrenheit: {f2:.2f}°F")
print(f"Kelvin: {k2:.2f} K\n")

print(f"Diferencia de temperaturas: {Diferencia:.2f}°C")