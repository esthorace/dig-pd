def set_mayusculas(texto: str) -> str | None:
    """Convierte una cadena a mayúsculas o devuelve None si el parámetro es una cadena vacía"""
    if not texto:
        return None
    return texto.upper()


def main() -> None:
    entrada = input("Ingresa una cadena: ")
    resultado = set_mayusculas(entrada)
    if resultado is None:
        print("La cadena está vacía")
        return
    print(f"Resultado: {resultado}")


main()
