from dataclasses import dataclass

# class Producto:
#     def __init__(self, nombre: str, precio: float, stock: int = 0) -> None:
#         self.nombre = nombre
#         self.precio = precio
#         self.stock = stock


@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int = 0


p1 = Producto(nombre="Laptop", precio=1200, stock=5)
print(p1)
