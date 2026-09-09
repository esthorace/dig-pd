class Usuario:
    sistema: str = "Django"  # variable de clase

    def __init__(self, username: str) -> None:
        self.username = username  # variable de instancia


admin = Usuario(username="admin")
user = Usuario(username="user")

print(admin.sistema)
print(user.sistema)

# ERROR
# admin.sistema = "FastAPI"  # Esto crea una variable de instancia en tiempo de ejecución
Usuario.sistema = "FastAPI"
print()
print(admin.sistema)
print(user.sistema)

print(vars(admin))
print(vars(user))
