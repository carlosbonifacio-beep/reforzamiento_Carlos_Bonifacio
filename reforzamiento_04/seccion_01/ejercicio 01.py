"""
Ejercicio 01. División segura
"""

def division_segura(a, b):
    return a / b

def ejecutar_prueba():
    try:
        num1 = float(input("Ingrese el numerador: "))
        num2 = float(input("Ingrese el denominador: "))
        resultado = division_segura(num1, num2)
        print(f"Resultado de la división: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")
    except ValueError:
        print("Error: Debe ingresar valores numéricos")
    finally:
        print("Operación finalizada")

for i in range(1, 4):
    print(f"--- Prueba {i} ---")
    ejecutar_prueba()