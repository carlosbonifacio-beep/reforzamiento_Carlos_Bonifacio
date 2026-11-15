#Calculo de indice de masa corporal
nombre = "Andrea Rivas"
peso = 68.0
estatura = 1.68

# IMC
imc = peso / (estatura ** 2)

# Clasificación según rangos de IMC
if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 25:
    clasificacion = "Peso normal"
elif 25 <= imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

# Reporte
print(f"Nombre: {nombre}")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"IMC calculado: {imc:.2f}")
print(f"Clasificación: {clasificacion}")