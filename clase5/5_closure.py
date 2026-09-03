def crear_multiplicador(n: int):
    def multiplicar(x: int):
        return x * n

    return multiplicar


duplicar = crear_multiplicador(2)
print(duplicar(10))

triplicar = crear_multiplicador(3)
print(triplicar(10))
