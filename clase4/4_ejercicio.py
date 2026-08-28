"""
Crear una función que reciba un diccionario y transformar sus
valores en mayúsculas.
Se debe crear un diccionario con 2 elementos cuyos valores sean cadenas.
Pasarlo como argumento a la función.
Debo guardar en una variable la devolución de la función.
Imprimir el diccionario original y luego el transformado.
"""


def convertir_mayusculas(diccionario: dict[str, str]) -> dict[str, str]:
    """Convierte los valores de un diccionario a mayúsculas"""
    for clave, valor in diccionario.items():
        diccionario[clave] = valor.upper()
    return diccionario


def main() -> None:
    diccionario_original = {"nombre": "Juan", "apellido": "Pérez"}
    diccionario_transformado = convertir_mayusculas(diccionario_original.copy())
    print(diccionario_original)
    print(diccionario_transformado)


main()
