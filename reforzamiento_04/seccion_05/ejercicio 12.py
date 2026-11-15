"""
Ejercicio 12. Cálculo de antigüedad laboral
"""
from datetime import datetime

def calcular_antiguedad(fecha_ingreso):
    fecha_actual = datetime.now()
    anios = fecha_actual.year - fecha_ingreso.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_ingreso.month, fecha_ingreso.day):
        anios -= 1
    return max(0, anios)

def calcular_aumento(sueldo_actual, anios_antiguedad):
    if anios_antiguedad > 3:
        porcentaje = 20
        monto_aumento = sueldo_actual * 0.20
    else:
        porcentaje = 0
        monto_aumento = 0.0
    sueldo_final = sueldo_actual + monto_aumento
    return porcentaje, monto_aumento, sueldo_final

for i in range(1, 4):
    print(f"\n=== Empleado {i} ===")
    try:
        nombre = input("Nombre del empleado: ")
        sueldo = float(input("Sueldo actual: "))
        fecha_str = input("Fecha de ingreso (DD/MM/AAAA): ")

        fecha_ingreso = datetime.strptime(fecha_str, "%d/%m/%Y")
        fecha_actual = datetime.now()

        anios = calcular_antiguedad(fecha_ingreso)
        porcentaje, aumento, sueldo_final = calcular_aumento(sueldo, anios)

        print("\n--- Resumen Salarial ---")
        print(f"Empleado: {nombre}")
        print(f"Fecha de ingreso: {fecha_ingreso.strftime('%d/%m/%Y')}")
        print(f"Fecha actual: {fecha_actual.strftime('%d/%m/%Y')}")
        print(f"Años de antigüedad: {anios} años")
        print(f"Sueldo original: S/. {sueldo:.2f}")
        print(f"Porcentaje aplicado: {porcentaje}%")
        print(f"Monto del aumento: S/. {aumento:.2f}")
        print(f"Sueldo final: S/. {sueldo_final:.2f}")
    except ValueError:
        print("Error: Formato de sueldo o fecha inválido. Use DD/MM/AAAA para la fecha.")