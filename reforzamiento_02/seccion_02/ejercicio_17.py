usuario_1 = []
usuario_2 = []

# Carga de datos con append() e insert()
usuario_1.append("David")
usuario_1.append("Bautista")
usuario_1.insert(2, 22)
usuario_1.append("Contador")

usuario_2.append("Ximena")
usuario_2.append("Delgado")
usuario_2.insert(2, 21)
usuario_2.append("Administradora")

print(f"Usuario 1: {usuario_1}")
print(f"Usuario 2: {usuario_2}")

# Suma de edades por índice (índice 2)
suma_edades = usuario_1[2] + usuario_2[2]
print(f"Suma de edades: {suma_edades}")

# Concatenar listas
concatenada = usuario_1 + usuario_2
print(f"Lista concatenada: {concatenada}")

# Lista en orden inverso
invertida = concatenada.copy()
invertida.reverse()
print(f"Lista en orden inverso: {invertida}")

# Modificaciones sobre la lista concatenada original
# 'concatenada' es: ['David', 'Bautista', 22, 'Contador', 'Ximena', 'Delgado', 21, 'Administradora']
# 1. Eliminar edad de usuario 1 (22)
concatenada.remove(22)
# 2. Eliminar apellido paterno de usuario 2 ('Delgado'). Tras borrar 22, 'Delgado' pasa al índice 4
concatenada.pop(4)

# 3. Actualizar la profesión del usuario 2 a "Analista de Datos" (índice 5 resultante)
concatenada[5] = "Analista de Datos"

# Salidas finales
print(f"Lista final modificada: {concatenada}")
print(f"Cantidad final de elementos: {len(concatenada)}")