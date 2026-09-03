import time


def medir_tiempo(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(resultado)
        print(f"⏱ Tiempo de ejecución: {fin - inicio:.4f} segundos")
        return resultado

    return wrapper


@medir_tiempo
def calcular():
    suma = 0
    for i in range(1_000_000):
        suma += i
    return suma


@medir_tiempo
def calcular2():
    multiplicacion = 2
    for i in range(1_000):
        multiplicacion *= 2
    return multiplicacion


calcular()
calcular2()
