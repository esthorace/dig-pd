from .inventario import vender


def vender_interactivo(inventario: dict) -> dict:
    producto = input("¿Producto que busca? ").lower().strip()
    if producto not in inventario:
        print(f"- El producto {producto} no está disponible")
        return inventario

    try:
        cantidad = int(input("¿Cuántas unidades quiere comprar? "))
    except ValueError:
        print("- Cantidad inválida")
        return inventario

    if cantidad > inventario[producto]:
        print(f"- No hay la cantidad suficiente. Restan {inventario[producto]}")
        return inventario

    return vender(inventario, producto, cantidad)
