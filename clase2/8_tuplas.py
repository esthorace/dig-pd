from math import pi

tupla = (1, -2, pi, "cadena", True, ("a", ""), None)

# Crear una tupla vacía
tupla = ()
tupla = tuple()
print("tupla vacía:", tupla)

# Crear una tupla con un solo elemento
tupla = (1,)
print("tupla con un solo elemento:", tupla)

# Acceder a los elementos de la tupla
tupla = ("Hola", "Mundo", "Python")
print("Elemento 0:", tupla[0])
print("Elemento 1:", tupla[1])
print("Elemento 2:", tupla[2])

# No puedo modificar los elementos de la tupla
# tupla[0] = "Hola!!!!"
# print("tupla:", tupla)

# Operador in verifica si un elemento está en la tupla
print("Python" in tupla)
print("JavaScript" in tupla)

# Unpacking (desempaquetar) la tupla
tupla = ("Hola", "Mundo", "Python")
saludo, mundo, lenguaje = tupla
print("saludo:", saludo)
print("mundo:", mundo)
print("lenguaje:", lenguaje)

# Concatenar tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print("tupla3:", tupla3)

# Unpacking (desempaquetar) la tupla con *
numeros_primos = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
primero, segundo, *resto = numeros_primos
print("primero:", primero)
print("segundo:", segundo)
print("resto:", resto)

# Unpacking (desempaquetar) la tupla con *
cartas = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
primera, *las_del_medio, ultima = cartas
print("primera:", primera)
print("las_del_medio:", las_del_medio)
print("ultima:", ultima)
