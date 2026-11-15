# Ejercicio 01: Control de inventario

productos = ["Arroz", "Azúcar", "Aceite", "Leche", "Fideos"]
cantidades = [8, 3, 12, 2, 6]

print("Productos registrados:")
total_unidades = 0
stock_bajo = False

for i in range(len(productos)):
    print(f"{productos[i]}: {cantidades[i]} unidades")
    total_unidades += cantidades[i]

print(f"Total de unidades disponibles: {total_unidades}")

print("Productos con menos de 5 unidades:")
for i in range(len(productos)):
    if cantidades[i] < 5:
        print(f"- {productos[i]}: {cantidades[i]} unidades")
        stock_bajo = True

if not stock_bajo:
    print("Ningún producto tiene stock bajo.")