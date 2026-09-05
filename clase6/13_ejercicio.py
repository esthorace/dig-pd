"""
Diseñar un sistema de clases en Python que modele dispositivos electrónicos
implementando herencia simple y herencia múltiple mediante un mixin:
crear una clase base Dispositivo con el método encender(),
una clase hija SmartWatch que añada el método medir_pasos(),
un mixin ConectividadWiFiMixin con los métodos conectar_red() y desconectar_red(),
y una clase CamaraIP que herede de ambos para verificar la reutilización de métodos
instanciando los objetos correspondientes y ejecutando sus comportamientos.

- instanciar SmartWatch
- instanciar CamaraIP
"""


class Dispositivo:
    def encender(self):
        print("El dispositivo se ha encendido.")


class SmartWatch(Dispositivo):
    def medir_pasos(self):
        print("Midiendo pasos...")


class ConectividadWiFiMixin:
    def conectar_red(self):
        print("Conectando a la red Wi-Fi...")

    def desconectar_red(self):
        print("Desconectando de la red Wi-Fi...")


class CamaraIP(Dispositivo, ConectividadWiFiMixin):  # herencia múltiple con mixin
    pass


smartwatch = SmartWatch()
smartwatch.encender()
smartwatch.medir_pasos()

camara_ip = CamaraIP()
camara_ip.encender()
camara_ip.conectar_red()
camara_ip.desconectar_red()
