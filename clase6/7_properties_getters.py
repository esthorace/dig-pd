class Usuario:
    def __init__(self, nombre: str, contraseña: str) -> None:
        self.nombre = nombre
        self.contraseña = contraseña

    def __str__(self) -> str:
        return f"{self.nombre} | {self.contraseña}"

    @property
    def contraseña(self):  # es un getter
        return self.__contraseña

    @property
    def contraseña_oculta(self):  # es un getter
        return "*" * len(self.__contraseña)

    @contraseña.setter
    def contraseña(self, nuevo_valor: str):  # es un setter
        if len(nuevo_valor) < 8:
            raise ValueError("La contraseña no puede tener menos de 8 caracteres")
        self.__contraseña = nuevo_valor  # ✨ Crea el atributo en la memoria del objeto


usuario = Usuario("Cin", "12345678")
print(usuario)
usuario.contraseña = "12345678"
print(usuario.contraseña)
print(usuario.contraseña_oculta)
