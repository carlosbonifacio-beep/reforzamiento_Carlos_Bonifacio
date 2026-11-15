"""
Módulo
"""

def validar_usuario(nombre_usuario):
    if len(nombre_usuario) < 7:
        return "El nombre de usuario debe contener al menos 7 caracteres"
    if len(nombre_usuario) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres"
    if not nombre_usuario.isalnum():
        return "El nombre de usuario puede contener solo letras y números"
    return True