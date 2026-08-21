def procesar_comando(comando):
    partes = comando.split()
    match partes:
        case []:
            print("No se ingresó ningún comando.")
        case ["salir"]:
            print("Saliendo del sistema...")
        case ["ayuda"]:
            print(
                "Comandos disponibles: ver, agregar <producto>, pagar <monto> <metodo>, salir"
            )
        case ["ver"]:
            print("Mostrando el carrito de compras...")
        case ["agregar", producto]:
            print(f"Producto '{producto}' agregado al carrito.")
        case ["pagar", monto, metodo]:
            print(f"Procesando pago de ${monto} con {metodo}...")
        case _:
            print("Comando no reconocido. Escriba 'ayuda' para ver las opciones.")


procesar_comando("")
procesar_comando("agregar manzanas")
procesar_comando("pagar 1500 efectivo")
procesar_comando("borrar todo")
procesar_comando("ayuda")
procesar_comando("salir")
