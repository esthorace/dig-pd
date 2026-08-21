# lista = [1, 100, 23]
lista = ["pan", 2000, "pan fresco recién sacado del horno", "buen gusto"]


match lista:
    case []:
        print("La lista está vacía")
    case [x]:
        print(f"La lista tiene un solo elemento: {x}")
    case [x, y]:
        print(f"La lista tiene dos elementos: {x} y {y}")
        print(f"La multiplicación de ambos es: {x * y}")
    case [producto, precio, *observaciones]:
        print("Nombre del producto:", producto)
        print("Precio:", precio)
        print("Observaciones:", " | ".join(observaciones))
    case _:
        print("No conozco esta estructura de datos")
