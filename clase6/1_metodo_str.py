class Usuario:
    def __init__(self, nombre: str, apellido: str) -> None:
        self.nombre = nombre
        self.apellido = apellido

    # Agregamos el método str
    def __str__(self) -> str:
        return f"Usuario: {self.nombre} {self.apellido}"


def main():
    usuario = Usuario(nombre="Juan", apellido="Pérez")
    print(usuario)


main()
