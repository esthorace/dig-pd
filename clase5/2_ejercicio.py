"""
Escribe una función llamada mostrar_perfil que utilice **kwargs
para recibir una cantidad variable de datos en formato clave-valor
y muestre en la consola cada clave junto con su valor en una línea independiente.
Comprueba su funcionamiento llamando a la función una vez con dos datos (como nombre y edad)
y otra vez con tres datos diferentes (como curso, nota y aprobado).
"""

from typing import Any


def mostrar_perfil(**kwargs: Any):
    for k, v in kwargs.items():
        print(f"{k.upper()}: {v}")


def main():
    mostrar_perfil(nombre="Juan", edad=30)
    mostrar_perfil(nombre="Luis", nota=2.4, aprobado=False)


main()
