numeros = [1, 2, 3, 4, 5, 6]

# numeros_pares = []
# for numero in numeros:
#     if numero % 2 == 0:
#         numeros_pares.append(numero)

numeros_pares = [numero for numero in numeros if numero % 2 == 0]

print(numeros)
print(numeros_pares)
