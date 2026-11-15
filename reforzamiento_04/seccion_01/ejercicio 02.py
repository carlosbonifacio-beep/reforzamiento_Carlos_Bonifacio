"""
Ejercicio 02. Actualización de elementos de una lista
"""

numeros = [2, 6, 10, 4, 5, 23, 1]

def actualizar_elemento(lista, indice, valor):
    if type(valor) is not int:
        raise TypeError("Error: El nuevo valor debe ser un número entero.")

    if indice < 0:
        raise IndexError("Error: No se admiten índices negativos.")

    lista[indice] = valor

for prueba in range(1, 5):
    print(f"\n--- Prueba {prueba} (Lista actual: {numeros}) ---")
    try:
        indice_input = input("Ingrese el índice a modificar: ")

        indice = int(indice_input)

        valor_input = input("Ingrese el nuevo valor entero: ")

        try:
            nuevo_valor = int(valor_input)
        except ValueError:
            nuevo_valor = valor_input

        actualizar_elemento(numeros, indice, nuevo_valor)
        print(f"Actualización exitosa. Lista resultante: {numeros}")

    except ValueError:
        print("Error: El índice ingresado debe ser un número entero válido (ValueError).")
    except IndexError as e:
        print(f"Error de rango: El índice está fuera de los límites de la lista (0 a {len(numeros) - 1}). {e}")
    except TypeError as e:
        print(f"Error de tipo: {e}")