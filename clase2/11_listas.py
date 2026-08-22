# Colección mutable de objetos indexados

lista = [1, 2, 3, "hola", True, 3.14, [1, 2, 3], ("a",)]
print(f"{lista = }")

# Crear una lista vacía
lista_vacia = []
print(f"{lista_vacia = }")
lista_vacia = list()
print(f"{lista_vacia = }")

# Crear (create)
lista = lista + ["fin"]
print(f"{lista = }")

lista += ["fin otra vez"]
print(f"{lista = }")

# Leer (read)
hola = lista[3]
print(f"{hola = }")

# Modificar (update)
lista[0] = {"curso": "Python"}
print(f"{lista = }")

# Eliminar (delete)
del lista[0]
print(f"{lista = }")
