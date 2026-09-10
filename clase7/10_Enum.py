from enum import Enum

# estados_pedido = ("pendiente", "enviado", "entregado")
# estado_actual = estados_pedido[0]

# if estado_actual == "pendiente":
#     print("El paqueste está pendiente de ser enviado")


class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"


estado_actual = EstadoPedido.PENDIENTE

if estado_actual == EstadoPedido.PENDIENTE:
    print("El paqueste está pendiente de ser enviado")
