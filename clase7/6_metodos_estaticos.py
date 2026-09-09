class Usuario:
    sistema: str = "Django"  # variable de clase

    def __init__(self, username: str) -> None:
        self.username = username  # variable de instancia

    @classmethod
    def cambiar_sistema(cls, nuevo_valor: str):
        if not nuevo_valor:
            print("-> No se ha cambiado la variable de clase porque la cadena está vacía")
            return
        cls.sistema = cls._encriptar_caracteres(nuevo_valor)

    @staticmethod
    def _encriptar_caracteres(caracters: str) -> str:
        return caracters[::-1]

    @staticmethod
    def info():
        print("Hola, soy un método estático")


admin = Usuario(username="admin")
admin.cambiar_sistema("FastAPI")
print(admin.sistema)
admin.info()
Usuario.info()
