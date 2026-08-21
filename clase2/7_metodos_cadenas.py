que_es_python = " pithon es un lenguaje de programación interpretado  "

# upper() convierte a mayusculas
print("upper():", que_es_python.upper())
# lower() convierte a minusculas
print("lower():", que_es_python.lower())
# title() convierte la primera letra de cada palabra en mayuscula
print("title():", que_es_python.title())

# strip() elimina los espacios en blanco al inicio y al final
print("strip():", que_es_python.strip())

# capitalize() convierte la primera letra en mayuscula
print("capitalize():", que_es_python.strip().capitalize())

# count() cuenta la cantidad de veces que aparece un caracter en una cadena
print("count():", que_es_python.count("o"))
print("count():", que_es_python.count("pithon"))

# isdigit() verifica si la cadena es un numero
print("isdigit():", "12345".isdigit())
print("isdigit():", "12345a".isdigit())

que_es_python = " pithon es un lenguaje de programación interpretado  "
# replace() reemplaza un caracter por otro
print("replace():", que_es_python.replace("pithon", "python"))
print("replace():", que_es_python.replace("e", "3"))

# split() divide la cadena en una lista de subcadenas
print("split():", que_es_python.split())

# join() une una lista de subcadenas en una cadena
print("join():", "-".join(["Django", "Python", "Flask"]))
