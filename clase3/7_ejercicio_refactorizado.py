from paquete_ia import (
    agregar_producto,
    agregar_productos,
    comprar,
    total_productos,
    vender,
    vender_interactivo,
)


def main():
    inventario = {"manzanas": 10, "naranjas": 5, "peras": 8}
    print(inventario)

    inventario = comprar(inventario, "manzanas", 5)
    print(inventario)

    inventario = vender(inventario, "naranjas", 3)
    print(inventario)

    inventario = agregar_producto(inventario, "uvas", 5)
    print(inventario)

    inventario = vender_interactivo(inventario)
    print(inventario)

    nuevos = {"frutillas": 20, "bananas": 10, "mandarinas": 5}
    inventario = agregar_productos(inventario, nuevos)
    print(inventario)

    print(f"El número total de productos es {total_productos(inventario)}")


if __name__ == "__main__":
    main()
