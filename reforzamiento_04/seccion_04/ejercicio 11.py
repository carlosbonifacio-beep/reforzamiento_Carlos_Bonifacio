"""
Ejercicio 11. Decorador para conteo y validación de argumentos
"""

def conteo_parametros(func):
    def wrapper(*args, **kwargs):
        total_argumentos = len(args) + len(kwargs)
        print(f"Cantidad total de argumentos recibidos: {total_argumentos}")

        todos_los_valores = list(args) + list(kwargs.values())

        son_validos = all(type(x) is int for x in todos_los_valores)

        if not son_validos:
            print("Solo se admiten números enteros. No se podrá realizar la suma")
        else:
            resultado = func(*args, **kwargs)
            print(f"Resultado de la suma: {resultado}")

        print("La función decoradora terminó de ejecutarse correctamente\n")

    return wrapper

@conteo_parametros
def sumar_enteros(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

print("--- Prueba 1: Solo posicionales ---")
sumar_enteros(10, 20, 30, 40)

print("--- Prueba 2: Combinación args y kwargs ---")
sumar_enteros(5, 15, x=25, y=35)

print("--- Prueba 3: Valores no válidos ---")
sumar_enteros(10, 5.5, flag=True)