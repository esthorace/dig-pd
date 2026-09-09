class Usuario:
    sistema: str = "Django"  # variable de clase

    def __init__(self, username: str) -> None:
        self.username = username  # variable de instancia

    @classmethod
    def cambiar_sistema(cls, nuevo_valor: str):
        if not nuevo_valor:
            print("-> No se ha cambiado la variable de clase porque la cadena está vacía")
            return
        cls.sistema = nuevo_valor


admin = Usuario(username="admin")
user = Usuario(username="user")

print(admin.sistema)
print(user.sistema)

# Usuario.sistema = "FastAPI"
# Usuario.cambiar_sistema("")
Usuario.cambiar_sistema("FastAPI")
print()
print(admin.sistema)
print(user.sistema)

print(vars(admin))
print(vars(user))
