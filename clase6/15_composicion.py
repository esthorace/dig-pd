class Motor:
    def __init__(self) -> None:
        self.esta_encendido: bool = False

    def iniciar(self):
        self.esta_encendido = True
        print("⚙️  Motor encendido.")

    def detener(self):
        self.esta_encendido = False
        print("⚙️  Motor detenido.")


class Auto:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.motor = Motor()  # composición

    def arrancar(self):
        if self.motor.esta_encendido:
            print("⚠️  Quieres arrancar el auto que ya ESTÁ en marcha.")
            return
        self.motor.iniciar()
        print(f"🚗 El auto {self.nombre} ha arrancado.")

    def apagar(self):
        if not self.motor.esta_encendido:
            print("⚠️  Quieres apagar el auto que ya NO está en marcha.")
            return
        self.motor.detener()
        print(f"🚗 El auto {self.nombre} se he detenido.")


auto = Auto("Ford Mustang")
auto.arrancar()
auto.arrancar()
auto.apagar()
auto.apagar()
