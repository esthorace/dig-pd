# archivo = open("14-test.txt", "w")
# archivo.write("Python\n")
# archivo.write("Django\n")
# archivo.close()

with open("14-test.txt", "w") as f:
    f.write("Python\n")
    f.write("Django\n")
    # no hace falta usar close()

# archivo = None
# try:
#     archivo = open("13_test.tx", "r")
#     contenido = archivo.read()
# except FileNotFoundError:
#     print("Error: El archivo no existe.")
# else:
#     print(contenido)
# finally:
#     if archivo is not None:
#         archivo.close()
try:
    with open("14-test.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError:
    print("Error: El archivo no existe.")
except Exception as e:
    print(f"Error inesperado: {repr(e)}")
else:
    print(contenido)
