def dividir(dividendo: float, divisor: float) -> tuple[float, float]:
    division = dividendo / divisor
    resto = dividendo % divisor
    return division, resto


def main() -> None:
    print(type(dividir(10, 3)))
    division, resto = dividir(10, 3)
    print(f"División: {division}\nResto: {resto}")


main()
