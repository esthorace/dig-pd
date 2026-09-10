from typing import Protocol


class PasarelaPago(Protocol):
    def pagar(self, monto: float) -> None:
        pass


class MercardoPagoService:
    def pagar(self, monto: float) -> None:
        # lógica de la API de MP
        print(f"[MercadoPago] procesando el pago de ${monto}")


class MODOService:
    def pagar(self, monto: float) -> None:
        # lógica de la API de MODO
        print(f"[MODO] procesando el pago de ${monto}")


def procesar_pago(pasarela: PasarelaPago, monto: float):
    print("Iniciando transacción...")
    pasarela.pagar(monto)
    print("Fin de transacción")


pasarela_mp = MercardoPagoService()
pasarela_modo = MODOService()

procesar_pago(pasarela_mp, 100)
procesar_pago(pasarela_modo, 200)
