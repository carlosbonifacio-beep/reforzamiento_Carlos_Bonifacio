# Reorganizacion de invitados

invitados = ['Luis', 'Ana', 'Raúl', 'Pedro', 'Miguel', 'Katherine', 'Fiorella']

# Separar según la longitud del nombre
impares = [nombre for nombre in invitados if len(nombre) % 2 != 0]
pares = [nombre for nombre in invitados if len(nombre) % 2 == 0]

# Combinar ambas listas
reorganizada = impares + pares

# Mostrar
print(f"Lista original: {invitados}")
print(f"Nombres con longitud impar: {impares}")
print(f"Nombres con longitud par: {pares}")
print(f"Lista reorganizada: {reorganizada}")