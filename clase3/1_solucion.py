matriz = [[1, 2, 3], [4, 5, 6]]

# lista_aplanada = []
# for lista in matriz:
#     for numero in lista:
#         lista_aplanada.append(numero)

lista_aplanada = [numero for lista in matriz for numero in lista]

print(lista_aplanada)
