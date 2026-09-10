from typing import TypedDict


class UsuarioDict(TypedDict):
    nombre: str
    edad: int
    activo: bool


# Crear un diccionario que sigue esa estructura

usuario: UsuarioDict = {
    "nombre": "Carlitos",
    "edad": 23,
    "activo": True,
}

print(usuario)
print(usuario["nombre"])
