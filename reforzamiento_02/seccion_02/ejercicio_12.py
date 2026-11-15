#Operaciones estadisticas con una lista numerica

departamentos = ["Lima", "Cusco", "Arequipa", "Piura", "Ica", "Puno"]
print(f"Lista original: {departamentos}")

buscar = "Piura"
nuevo = "Tacna"

# Búsqueda y reemplazo por índice
if buscar in departamentos:
    posicion = departamentos.index(buscar)
    departamentos[posicion] = nuevo
    print(f"Departamento a reemplazar: {buscar}")
    print(f"Nuevo departamento: {nuevo}")
else:
    print(f"El departamento '{buscar}' no fue encontrado.")

print(f"Lista actualizada: {departamentos}")
print(f"Cantidad de departamentos: {len(departamentos)}")