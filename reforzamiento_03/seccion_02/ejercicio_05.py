# Ejercicio 05: Eliminación de un elemento de una lista

def eliminar_primer_elemento(lista, valor):
    nueva_lista = lista.copy()
    if valor in nueva_lista:
        nueva_lista.remove(valor)
    return nueva_lista

numeros = [10, 20, 30, 20, 40]
valor_existente = 20
valor_inexistente = 50

resultado_existente = eliminar_primer_elemento(numeros, valor_existente)
print(f"Lista original: {numeros}")
print(f"Buscando eliminar '{valor_existente}': {resultado_existente}")

resultado_inexistente = eliminar_primer_elemento(numeros, valor_inexistente)
print(f"Buscando eliminar '{valor_inexistente}': {resultado_inexistente}")
print(f"Verificando que la lista original no cambió: {numeros}")