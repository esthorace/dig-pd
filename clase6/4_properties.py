class Usuario:
    def __init__(self, nombre: str, contraseña: str) -> None:
        self._nombre = nombre
        self.contraseña = contraseña

    # def set_nombre(self, nuevo_valor: str):
    #     if not nuevo_valor:
    #         raise ValueError("No puede estar vacío")
    #     self.nombre = nuevo_valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_valor: str):
        if not nuevo_valor:
            raise ValueError("No puede estar vacío")
        self._nombre = nuevo_valor


usuario = Usuario("admin", "123")
print(usuario.nombre)
# usuario.set_nombre("superadmin")
usuario.nombre = "superadmin"
print(usuario.nombre)
