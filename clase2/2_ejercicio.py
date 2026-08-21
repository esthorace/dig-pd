"""
A partir del ejercicio anterior:
Implementar funciones
"""


def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            return int(entrada)


def es_mayor_edad(edad):
    return edad >= 18


def solicitar_datos():
    edad = pedir_entero("Ingrese su edad: ")

    # Retorno temprano: para no solicitar más datos
    if not es_mayor_edad(edad):
        return 0, 0, 0

    antiguedad = int(input("Ingrese su antigüedad en el sistema financiero: "))
    ingresos = float(input("Ingrese su ingreso mensual: "))

    return edad, antiguedad, ingresos


def es_perfil_estandar(antiguedad, ingresos):
    return antiguedad >= 3 and ingresos > 2500


def es_perfil_premium(ingresos):
    return ingresos >= 4000


def evaluar_credito(edad_suficiente, antiguedad, ingresos):
    if not edad_suficiente:
        return False
    return es_perfil_estandar(antiguedad, ingresos) or es_perfil_premium(ingresos)


def main():
    edad, antiguedad, ingresos = solicitar_datos()
    es_credito_aprobado = evaluar_credito(edad, antiguedad, ingresos)
    if es_credito_aprobado:
        print("Crédito aprobado")
    else:
        print("Rechazado")


main()
