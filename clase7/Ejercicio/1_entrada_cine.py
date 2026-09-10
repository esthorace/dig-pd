import json


class EntradaCine:
    def __init__(self, pelicula: str, funcion: str, asiento: str, precio: float):
        self.pelicula = pelicula
        self.funcion = funcion
        self.asiento = asiento
        self.precio = precio
        self.usada = False

    def usar_entrada(self):
        if not self.usada:
            self.usada = True
            print(f"Entrada para '{self.pelicula}' validada correctamente.")
        else:
            print("Esta entrada ya ha sido utilizada.")

    def cambiar_asiento(self, nuevo_asiento: str):
        if not self.usada:
            self.asiento = nuevo_asiento
            print(f"Asiento cambiado exitosamente a {self.asiento}.")
        else:
            print("No se puede cambiar el asiento de una entrada ya usada.")

    def to_json(self) -> str:
        datos = {
            "pelicula": self.pelicula,
            "funcion": self.funcion,
            "asiento": self.asiento,
            "precio": self.precio,
            "usada": self.usada,
        }
        return json.dumps(datos, indent=4, ensure_ascii=False)


# Ejemplo de uso e interacción
mi_entrada = EntradaCine(pelicula="Matrix", funcion="21:30 Hs", asiento="F12", precio=4500.0)

# Salida del JSON inicial
print("--- JSON Inicial ---")
print(mi_entrada.to_json())

# Cambio de asiento y validación
mi_entrada.cambiar_asiento("H08")
mi_entrada.usar_entrada()

# Salida del JSON actualizado
print("\n--- JSON Actualizado ---")
print(mi_entrada.to_json())
