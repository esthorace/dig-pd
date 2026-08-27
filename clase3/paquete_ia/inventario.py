def comprar(inventario: dict, producto: str, cantidad: int) -> dict:
    inventario[producto] = inventario.get(producto, 0) + cantidad
    return inventario


def vender(inventario: dict, producto: str, cantidad: int) -> dict:
    if producto not in inventario:
        return inventario
    if cantidad > inventario[producto]:
        return inventario
    inventario[producto] -= cantidad
    return inventario


def agregar_producto(inventario: dict, producto: str, cantidad: int) -> dict:
    inventario[producto] = cantidad
    return inventario


def agregar_productos(inventario: dict, nuevos: dict) -> dict:
    inventario.update(nuevos)
    return inventario


def total_productos(inventario: dict) -> int:
    return sum(inventario.values())
