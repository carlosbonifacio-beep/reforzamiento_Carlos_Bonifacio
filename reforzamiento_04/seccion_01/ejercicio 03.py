"""
Ejercicio 03. Consulta de información personal
"""

persona = {
    "nombre": "Xavier",
    "apellido_paterno": "Rodriguez",
    "apellido_materno": "Gonzales",
    "dni": "63325345",
    "edad": 28,
    "correo": "xavier.rodriguez@gmail.com",
    "telefono": "987654321",
    "direccion": "Av. Los Olivos 450",
    "ciudad": "Lima",
    "profesion": "Ingeniero de Software",
    "empresa": "Tech Solutions",
    "salario": 4500.00,
    "estado_civil": "Soltero"
}

def consultar_dato(diccionario, clave):
    try:
        valor = diccionario[clave]
        print(f"Clave: '{clave}' -> Valor: {valor}")
    except KeyError:
        print("Error: La clave ingresada no existe en el diccionario")

print("Claves disponibles:", list(persona.keys()))

for i in range(1, 6):
    print(f"\n--- Consulta {i} ---")
    clave_buscada = input("Ingrese el nombre de la clave a consultar: ")
    consultar_dato(persona, clave_buscada)