"""
A partir de la siguiente lista:
matriz:

matriz = [
    [1, 20, 3],
    [4, 3, 2],
    [10, 4, 1],
]

Sumar los elementos de cada lista y agregar el resultado
al final de cada lista. Debe quedar de la siguiente forma:

matriz = [
    [1, 20, 3, 24],
    [4, 3, 2, 9],
    [10, 4, 1, 15],
]
"""

matriz = [[1, 20, 3], [4, 3, 2], [10, 4, 1]]
print(matriz)

# Alternativa I
matriz[0] = matriz[0] + [matriz[0][0] + matriz[0][1] + matriz[0][2]]
matriz[1] = matriz[1] + [matriz[1][0] + matriz[1][1] + matriz[1][2]]
matriz[2] = matriz[2] + [matriz[2][0] + matriz[2][1] + matriz[2][2]]
print(matriz)

# Alternativa II
matriz = [[1, 20, 3], [4, 3, 2], [10, 4, 1]]
matriz[0] += [sum(matriz[0])]
matriz[1] += [sum(matriz[1])]
matriz[2] += [sum(matriz[2])]
print(matriz)

# Alternativa III
matriz = [[1, 20, 3], [4, 3, 2], [10, 4, 1]]
matriz_nueva = []
for fila in matriz:
    fila.append(sum(fila))
    matriz_nueva.append(fila)
print(matriz_nueva)

# Alternativa IV
matriz = [[1, 20, 3], [4, 3, 2], [10, 4, 1]]
# matriz_nueva = []
# for fila in matriz:
#     fila.append(sum(fila))
#     matriz_nueva.append(fila)
matriz_nueva = [fila + [sum(fila)] for fila in matriz]
print(matriz_nueva)
