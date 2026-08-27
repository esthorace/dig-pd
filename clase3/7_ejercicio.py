"""

A partir del siguiente diccionario, realizar los ejercicios propuestos:

inventario = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 8
}

1. Se compraron 5 manzanas.
2. Se vendieron 3 naranjas.
3. Se compraron 5 uvas.
4. Solicitar al usuario qué producto está buscando, y, si está disponible,
pedir la cantidad, venderlo y mostrar el inventario. La cantidad no debe superar el stock.
5. Crear un nuevo diccionario con 3 productos, agregarlos al diccionario principal.
6. Calcular el número total de productos del inventario.
"""

inventario = {"manzanas": 10, "naranjas": 5, "peras": 8}
print(inventario)

# 1. Se compraron 5 manzanas.
inventario["manzanas"] += 5
print(inventario)

# 2. Se vendieron 3 naranjas.
inventario["naranjas"] -= 3
print(inventario)

# 3. Se compraron 5 uvas.
inventario["uvas"] = 5
print(inventario)

# 4. Solicitar al usuario qué producto está buscando, y, si está disponible,
# pedir la cantidad, venderlo y mostrar el inventario. La cantidad no debe superar el stock.
producto_buscado = input("¿Producto que busca? ").lower().strip()
if producto_buscado in inventario:
    cantidad = int(input("¿Cuántas unidades quiere comprar? "))
    if cantidad >= inventario.get(producto_buscado, 0):
        print(f"- No hay la cantidad suficiente. Restan {inventario[producto_buscado]}")
    else:
        print(
            f"✅  Venta realizada. Restan {inventario[producto_buscado]} {producto_buscado}"
        )
else:
    print(f"- El producto {producto_buscado} no está disponible")

# 5. Crear un nuevo diccionario con 3 productos, agregarlos al diccionario principal.
nuevos_productos = {
    "frutillas": 20,
    "bananas": 10,
    "mandarinas": 5,
}
# inventario = {**inventario, **nuevos_productos}
inventario.update(nuevos_productos)
print(inventario)

# 6. Calcular el número total de productos del inventario.
total_productos = sum(inventario.values())
print(f"El número total de productos es {total_productos}")
