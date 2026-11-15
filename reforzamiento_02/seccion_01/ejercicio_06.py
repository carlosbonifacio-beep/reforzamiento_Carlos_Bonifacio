# calculo del importe de una compra
#datos
Nombre = "Ximena"
Producto = "Crema"
Precio_unitario = 42.50
Cantidad = 3

#Subtotal de la compra
subtotal = Precio_unitario * Cantidad

#descuento del 10%
if Cantidad >= 3:
    Descuento = subtotal * 0.10
else:
    Descuento = 0.0

total_pagar = subtotal - Descuento

#mostrar compras
print(f"Nombre: {Nombre}")
print(f"Producto: {Producto}")
print(f"Precio unitario: S/{Precio_unitario:.2f}")
print(f"Cantidad: {Cantidad}")
print(f"subtotal: S/{subtotal:.2f}")
print(f"Descuento (10%): S/{Descuento:.2f}")
print(f"Total a pagar: S/{total_pagar:.2f}")
