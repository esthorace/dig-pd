"""
A partir del siguiente código, crear un bloque
try-except para que muestre "el archivo no existe"

archivo = open("13_test.txt", "w")
archivo.write("Python\n")
archivo.write("Django\n")
archivo.close()

archivo = open("13_test.tx", "r")
contenido = archivo.read()
archivo.close()
print(contenido)
"""

try:
    archivo = open("13_test.txt", "w")
    archivo.write("Python\n")
    archivo.write("Django\n")
    archivo.close()
except Exception as e:
    print("Error:", repr(e))


archivo = None
try:
    archivo = open("13_test.tx", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no existe.")
else:
    print(contenido)
finally:
    if archivo is not None:
        archivo.close()
