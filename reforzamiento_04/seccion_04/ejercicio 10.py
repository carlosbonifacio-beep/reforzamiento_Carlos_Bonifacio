"""
Ejercicio 10. Decorador para multiplicación de números
"""

def decorador_multiplicacion(func):
    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función")
        resultado = func(*args, **kwargs)
        print(f"Resultado de la multiplicación: {resultado}")
        print("La función ha sido ejecutada correctamente\n")
        return resultado
    return wrapper

@decorador_multiplicacion
def multiplicar_seis(a, b, c, d=1, e=1, f=1):
    return a * b * c * d * e * f

multiplicar_seis(2, 3, 4, d=1, e=2, f=5)
multiplicar_seis(1, 5, 2, d=3, e=3, f=2)
multiplicar_seis(10, 2, 1, d=4, e=5, f=1)