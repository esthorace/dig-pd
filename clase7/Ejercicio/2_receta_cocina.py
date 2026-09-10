import json


class RecetaCocina:
    def __init__(self, nombre: str, autor: str, tiempo_coccion: int, ingredientes: list):
        self.nombre = nombre
        self.autor = autor
        self.tiempo_coccion = tiempo_coccion
        self.ingredientes = ingredientes
        self.valoraciones = []

    def agregar_ingrediente(self, ingrediente: str):
        self.ingredientes.append(ingrediente)

    def agregar_valoracion(self, puntuacion: float):
        if 1.0 <= puntuacion <= 5.0:
            self.valoraciones.append(puntuacion)

    def to_json(self) -> str:
        datos = {
            "nombre": self.nombre,
            "autor": self.autor,
            "tiempo_coccion": self.tiempo_coccion,
            "ingredientes": self.ingredientes,
            "valoraciones": self.valoraciones,
        }
        return json.dumps(datos, indent=4, ensure_ascii=False)
