#reforzamiento
sueldo = 3200

#evaluar par e impar
if sueldo % 2 == 0:
    clasificacion = "numero par"
else:
    clasificacion = "numero impar"

#calculo de una variable equivalente al 12% del sueldo y el el sueldo total
bono = sueldo * 0.12
sueldo_total = sueldo + bono

#Residuo de dividir entre 7
Residuo = sueldo % 7

#Montos
print(f"sueldo inicial: S/{sueldo}")
print(f"clasificacion: {clasificacion}")
print(f"Bono (12%): S/{bono:.2f}")
print(f"Sueldo final: S/{sueldo_total:.2f}")
print(f"Residuo de dividir entre 7: {Residuo}")
