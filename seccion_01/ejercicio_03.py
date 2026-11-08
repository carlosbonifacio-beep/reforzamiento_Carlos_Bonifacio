# Ejercicio 03: Carrito de compras

precios = {"Teclado": 75, "Mouse": 45, "Audífonos": 120, "USB": 35}
carrito = ["Teclado", "Audífonos", "USB", "Monitor"]

print("Productos seleccionados:")
subtotal = 0

for producto in carrito:
    if producto in precios:
        precio = precios[producto]
        print(f"{producto}: S/{precio:.2f}")
        subtotal += precio
    else:
        print(f"El producto '{producto}' no está registrado en el inventario.")

descuento = 0
if subtotal > 200:
    descuento = subtotal * 0.10

total_a_pagar = subtotal - descuento

print(f"Subtotal: S/{subtotal:.2f}")
print(f"Descuento (10%): S/{descuento:.2f}")
print(f"Total a pagar: S/{total_a_pagar:.2f}")