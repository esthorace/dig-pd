import json


class CuentaBanco:
    def __init__(self, cbu: str, titular: str, saldo_inicial: float = 0.0):
        self.cbu = cbu
        self.titular = titular
        self.saldo = saldo_inicial
        self.activa = True
        self.historial = []

    def depositar(self, monto: float):
        if self.activa and monto > 0:
            self.saldo += monto
            self.historial.append(f"Depósito: +{monto}")

    def extraer(self, monto: float):
        if self.activa and 0 < monto <= self.saldo:
            self.saldo -= monto
            self.historial.append(f"Extracción: -{monto}")

    def to_json(self) -> str:
        datos = {
            "cbu": self.cbu,
            "titular": self.titular,
            "saldo": self.saldo,
            "activa": self.activa,
            "historial": self.historial,
        }
        return json.dumps(datos, indent=4, ensure_ascii=False)
