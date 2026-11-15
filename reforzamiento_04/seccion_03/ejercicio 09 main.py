"""
Ejercicio 09. Operaciones matemáticas mediante módulos
"""
from calculos import raiz_cuadrada, cuadrado, cubo

for prueba in range(1, 4):
    print(f"\n--- Prueba {prueba} ---")
    try:
        dato = float(input("Ingrese un número mayor o igual a cero: "))
        if dato < 0:
            print("Error: El número debe ser mayor o igual que cero.")
            continue

        print(f"Número ingresado: {dato}")
        print(f"Raíz cuadrada: {raiz_cuadrada(dato):.4f}")
        print(f"Cuadrado: {cuadrado(dato)}")
        print(f"Cubo: {cubo(dato)}")
    except ValueError:
        print("Error: Entrada no válida. Debe ingresar un valor numérico.")