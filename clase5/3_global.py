contador_global = 0  # ámbito global


def mostrar_contador():
    print(contador_global)


def incrementar_contador_global():
    global contador_global  # si no hago, python interpreta que va a utilizar una variable local
    contador_global += 1


mostrar_contador()
incrementar_contador_global()
incrementar_contador_global()
incrementar_contador_global()
mostrar_contador()
