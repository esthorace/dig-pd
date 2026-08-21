"""
A partir del ejercicio anterior
Mejorar UX
"""

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    antiguedad = int(input("Ingrese su antigüedad en el sistema financiero: "))
    ingreso = float(input("Ingrese su ingreso mensual: "))

    if (antiguedad >= 3 and ingreso > 2500) or ingreso >= 4000:
        print("Se aprueba el crédito")
    else:
        print("No se aprueba el crédito")
else:
    print("No se aprueba el crédito: No eres mayor de edad")
