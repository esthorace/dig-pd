def sumar(a: int, b: int, c: int = 0) -> int:
    """Suma tres números, el tercer parámetro es opcional y es por defecto 0"""
    return a + b + c


def main() -> None:
    resultado = sumar(1, 2)
    print(f"El resultado es {resultado}")

    resultado = sumar(1, 2, 3)
    print(f"El resultado es {resultado}")


main()
