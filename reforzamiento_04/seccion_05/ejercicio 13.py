"""
Ejercicio 13. Cálculo y seguimiento de fechas de vencimiento
"""
from datetime import datetime, timedelta

def calcular_vencimiento(fecha_inicial, plazo_dias):
    return fecha_inicial + timedelta(days=plazo_dias)

def evaluar_vencimiento(fecha_vencimiento):
    hoy = datetime.now().date()
    venc = fecha_vencimiento.date()
    diferencia = (venc - hoy).days

    if diferencia > 0:
        return f"PENDIENTE: Faltan {diferencia} días para el vencimiento."
    elif diferencia == 0:
        return "VENCE HOY: La obligación vence en la fecha actual."
    else:
        return f"VENCIDA: Han transcurrido {abs(diferencia)} días desde el vencimiento."

for i in range(1, 4):
    print(f"\n=== Evaluación de Obligación {i} ===")
    try:
        fecha_str = input("Ingrese la fecha inicial (DD/MM/AAAA): ")
        plazo = int(input("Ingrese el plazo en días (entero no negativo): "))

        if plazo < 0:
            print("Error: El plazo debe ser un número entero no negativo.")
            continue

        fecha_inicial = datetime.strptime(fecha_str, "%d/%m/%Y")
        fecha_vencimiento = calcular_vencimiento(fecha_inicial, plazo)
        fecha_actual = datetime.now()
        estado = evaluar_vencimiento(fecha_vencimiento)

        print("\n--- Detalle de Vencimiento ---")
        print(f"Fecha inicial: {fecha_inicial.strftime('%d/%m/%Y')}")
        print(f"Plazo: {plazo} días")
        print(f"Fecha de vencimiento: {fecha_vencimiento.strftime('%d/%m/%Y')}")
        print(f"Fecha actual: {fecha_actual.strftime('%d/%m/%Y')}")
        print(f"Estado: {estado}")
    except ValueError:
        print("Error: Verifique que la fecha tenga formato DD/MM/AAAA y el plazo sea entero.")