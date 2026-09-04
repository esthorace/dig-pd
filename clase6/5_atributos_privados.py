class Usuario:
    def __init__(self, nombre: str, contraseña: str) -> None:
        self.__nombre = nombre  # atributo privado
        self.contraseña = contraseña

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_valor: str):
        if not nuevo_valor:
            raise ValueError("No puede estar vacío")
        self.__nombre = nuevo_valor


usuario = Usuario("admin", "123")
print(f"{usuario.nombre = }")

# usuario.set_nombre("superadmin")
# usuario.nombre = ""
usuario.nombre = "superadmin"
print(f"{usuario.nombre = }")

# print(usuario.__nombre)
# usuario.__nombre = "hola!!!"  # !!!! crea una variable de instancia PÚBLICA
# print(usuario.__nombre)
# print(vars(usuario))
