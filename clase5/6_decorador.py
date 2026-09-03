# @decorador -> es una función que recibe una función y devuelve una función


from collections.abc import Callable


def mi_decorador(funcion: Callable) -> Callable:
    def envoltorio():
        print("Holaaa")
        funcion()
        print("Chauuu")

    return envoltorio


@mi_decorador
def saludar():
    print("Python es lo más!")


saludar()
