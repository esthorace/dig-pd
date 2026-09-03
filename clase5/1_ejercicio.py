"""
Crear una función que reciba argumentos indeterminados que
sean alturas de personas, crear una lista y ordenarla de menor a mayor
y devolver la lista ordenada
Usar isinstance para validar que los argumentos sean de tipo numerico
"""


def ordenar_alturas(*alturas: float) -> list[float]:
    alturas_lista = []
    for altura in alturas:
        if isinstance(altura, float | int):
            alturas_lista.append(altura)
    alturas_lista.sort()
    return alturas_lista


def main():
    alturas_lista_ordenada = ordenar_alturas(1.75, 1.80, 1.50, 1.60, "1.65", 2)
    print(alturas_lista_ordenada)


main()
