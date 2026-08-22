# Métodos de las listas

serie_fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
print("Serie de Fibonacci:", serie_fibonacci)

# **** CREATE
# append()
# Añade un elemento al final de la lista
numero_siguiente = serie_fibonacci[-1] + serie_fibonacci[-2]
serie_fibonacci.append(numero_siguiente)
print("append():", serie_fibonacci)

# extend()
# Añade los elementos de otra lista al final de la lista
serie_fibonacci.extend([233, 377, 610])
print("extend():", serie_fibonacci)

# # insert()
# # Añade un elemento en una posición específica
serie_fibonacci.insert(0, "INICIO")
print("insert():", serie_fibonacci)

# **** DELETE
# pop()
# Elimina el último elemento de la lista y lo devuelve
ultimo_elemento = serie_fibonacci.pop()
print("pop():", ultimo_elemento)
print("Serie de Fibonacci:", serie_fibonacci)

# # remove()
# Elimina el primer elemento que coincide con el valor
serie_fibonacci.remove(233)
print("remove():", serie_fibonacci)

# # clear()
# Elimina todos los elementos de la lista
# serie_fibonacci = []  # se usa para inicializar una lista vacía
serie_fibonacci.clear()
print("clear():", serie_fibonacci)

# **** UPDATE
# sort()
# Ordena los elementos de la lista
letras = ["c", "a", "b", "e", "d"]
letras.sort()
print("sort():", letras)

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numeros.sort(reverse=True)
print("sort(reverse=True):", numeros)
