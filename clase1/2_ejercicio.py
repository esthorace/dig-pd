"""
Una empresa debe aprobar o no un crédito para un cliente.
Las condiciones son las siguientes:
    - El cliente debe ser mayor de edad.
    - Debe tener una antigüedad en el sistema financiero mínimo de 3 años
    y un ingreso mayor a 2500 dólares.
    - En caso de que no tenga la antigüedad suficiente,
    su ingreso mensual debe ser como mínimo 4000 dólares.
Si no cumple ninguna de las condiciones, no se aprueba el crédito.

-> No usar funciones, ni try-except, ni POO
"""

# Entrada de datos
edad = int(input("Ingrese su edad: "))
antiguedad = int(input("Ingrese su antigüedad en el sistema financiero: "))
ingreso = float(input("Ingrese su ingreso mensual: "))

# Validación

# aprobado = edad >= 18 and ((antiguedad >= 3 and ingreso > 2500) or ingreso >= 4000)

es_mayor_edad = edad >= 18
caso_1 = es_mayor_edad and antiguedad >= 3 and ingreso > 2500
caso_2 = es_mayor_edad and ingreso >= 4000

# Salida
if caso_1 or caso_2:
    print("Se aprueba el crédito")
else:
    print("No se aprueba el crédito")
