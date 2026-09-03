"""
Manejo de excepciones

try:
    # código que puede lanzar una excepción
except:
    # código que se ejecuta si se lanza una excepción
else:
    # (opcional): código que se ejecuta si no se lanza una excepción
finally:
    # (opcional): código que se ejecuta siempre
"""

try:
    numero_1 = int(input("Número 1: "))
    numero_2 = int(input("Número 2: "))
    division = numero_1 / numero_2
except ValueError:
    print("Debes ingresar un número, no letras ni espacios")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as mensaje_error:
    print("Error.", type(mensaje_error))
else:
    print(division)
finally:
    print("👋")
