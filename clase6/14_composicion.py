class Motor:
    def iniciar(self):
        print("✅ Motor encendido")

    def detener(self):
        print("✅ Motor detenido")


class Auto:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.motor = Motor()  # composición

    def arrancar(self):
        self.motor.iniciar()
        print(f"El auto {self.nombre} ha arrancado.")

    def apagar(self):
        self.motor.detener()
        print(f"El auto {self.nombre} se he detenido.")


auto = Auto("Ford Mustang")
auto.arrancar()
auto.apagar()
