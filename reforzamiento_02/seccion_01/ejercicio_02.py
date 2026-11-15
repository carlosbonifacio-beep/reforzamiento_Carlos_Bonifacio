#variable
radio = 6.0
PI = 3.14159

"calculo"
diametro_1 = radio * 2
volumen_1 = (4/3) * PI * (radio ** 3)

#segunda esfera
radio_2 = radio * 2
volumen_2 = (4/3) * PI *(radio_2 ** 3)

#resultados
print(f"Radio de la primera esfera: {radio:.2f}")
print(f"Diametro de la primera esfera: {diametro_1:.2f}")
print(f"Volumen de la primera esfera: {volumen_1:.2f}")
print(f"Radio de la segunda esfera: {radio_2:.2f}")
print(f"Volumen de la segunda esfera: {volumen_2:.2f}")

