# def sumar(a: int, b: int, c: int = 0, d: int = 0):
#     return a + b + c + d


# def sumar(*numeros):
#     print(type(numeros))
#     return numeros


# def sumar(*numeros: float) -> float:
#     return sum(numeros)


def sumar(*args: float) -> float:
    return sum(args)


print(sumar(1, 200))
print(sumar(1, 200, 5000))
print(sumar(1, 200, 5000, 10000.3))
