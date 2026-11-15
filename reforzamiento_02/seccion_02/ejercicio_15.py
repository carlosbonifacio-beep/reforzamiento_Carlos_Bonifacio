#Eliminacion de elementos duplicados

original = ["Google", "Microsoft", "Amazon", "Oracle", "IBM"]
copia_empresas = original.copy()

# Agregar 3 elementos (2 duplicados)
copia_empresas.append("Google")
copia_empresas.append("Amazon")
copia_empresas.append("Meta")

# Crear lista sin duplicados conservando el orden de aparición
sin_duplicados = []
for empresa in copia_empresas:
    if empresa not in sin_duplicados:
        sin_duplicados.append(empresa)

duplicados_eliminados = len(copia_empresas) - len(sin_duplicados)

# Imprimir resultados
print(f"Lista original: {original}")
print(f"Lista con nuevos elementos: {copia_empresas}")
print(f"Lista sin duplicados: {sin_duplicados}")
print(f"Elementos duplicados eliminados: {duplicados_eliminados}")