"""
A partir del siguiente código, crear un método para cambiar el nombre:

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"
"""


class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"

    def set_nombre(self, nuevo_valor: str):
        if not nuevo_valor:
            print("✖️ No se puede cambiar de nombre: nuevo valor vacío")
            return
        self.nombre = nuevo_valor


def main():
    usuario1 = Usuario("Juan", "Pérez")
    usuario2 = Usuario("Marcos", "Roca")
    usuario3 = Usuario("Orlando", "Ríos")
    usuarios = (usuario1, usuario2, usuario3)
    for u in usuarios:
        print(u)
    usuario1.set_nombre("Juan Rodrigo")
    for u in usuarios:
        print(u)


main()
