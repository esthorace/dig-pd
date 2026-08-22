# Métodos de las tuplas

serie_fibonacci = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144)
print("Serie de Fibonacci:", serie_fibonacci)

# count()
print("count(1):", serie_fibonacci.count(1))

# index()
# Devuelve el índice del primer elemento que coincide con el valor
valor_buscado = 13
indice_del_valor_buscado = serie_fibonacci.index(valor_buscado)
print(f"El índice del valor buscado {valor_buscado} es: {indice_del_valor_buscado}")

# len()
print("len(serie_fibonacci):", len(serie_fibonacci))

# max()
print("max(serie_fibonacci):", max(serie_fibonacci))

# min()
print("min(serie_fibonacci):", min(serie_fibonacci))
