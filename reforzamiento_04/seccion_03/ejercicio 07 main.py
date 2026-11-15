"""
Ejercicio 07. Pruebas de validación de nombres de usuario
"""
from validaciones import validar_usuario

usuarios_prueba = [
    "user1",
    "usuario1234567",
    "user_name99",
    "xavier2026",
    "admin01"
]

for usuario in usuarios_prueba:
    resultado = validar_usuario(usuario)
    print(f"Usuario: '{usuario}' -> Resultado: {resultado}")