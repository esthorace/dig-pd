class Motor:
    def __init__(self, cilindradas: int) -> None:
        self.cilindradas = cilindradas

    def iniciar(self):
        print("✅ Motor encendido")

    def detener(self):
        print("✅ Motor detenido")


class Auto:
    def __init__(self, nombre: str, motor: Motor) -> None:
        self.nombre = nombre
        self.motor = motor  # agregación

    def arrancar(self):
        self.motor.iniciar()
        print(f"El auto {self.nombre} ha arrancado.")

    def apagar(self):
        self.motor.detener()
        print(f"El auto {self.nombre} se he detenido.")


motor = Motor(cilindradas=5000)
auto = Auto("Ford Mustang", motor)
auto.arrancar()
auto.apagar()

print("Cilindradas del auto:", auto.motor.cilindradas)
