"""
Ejercicio 08. Generación y análisis de números aleatorios
"""
from operaciones import generar_lista, ordenar_lista, obtener_mayor

lista_original = generar_lista()
lista_ordenada = ordenar_lista(lista_original)
numero_mayor = obtener_mayor(lista_original)

print("Lista original:", lista_original)
print("Lista ordenada:", lista_ordenada)
print("Número mayor:", numero_mayor)
print("Verificación lista original intacta:", lista_original)