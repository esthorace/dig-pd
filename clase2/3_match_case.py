numero = int(input("Ingrese un número: "))

# if numero == 1:
#     print("El número es 1")
# elif numero == 2:
#     print("El número es 2")
# elif numero == 3:
#     print("El número es 3")
# else:
#     print("El número no es 1, 2 o 3")

match numero:
    case 1:
        print("El número es 1")
    case 2:
        print("El número es 2")
    case 3:
        print("El número es 3")
    case _:
        print("El número no es 1, 2 o 3")
