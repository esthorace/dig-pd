# def my_upper(texto):
#     if texto != "":
#         return texto.upper()
#     else:
#         return "🚨  La cadena está vacía"


def my_upper(texto: str) -> str | None:
    """Convierte una cadena a mayúsculas o devuelve None si el parámetro es una cadena vacía"""
    if not texto:
        return None
    return texto.upper()


print(my_upper("  hola!!!"))
print(my_upper(""))
help(my_upper)
