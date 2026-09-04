class Guitarra:
    def tocar(self):
        print("tin tin tin")


class GuitarraElectrica(Guitarra):  # herencia
    # def tocar(self):
    #     print("tin tin tin")

    def tocar_con_distorsion(self):
        print("tron tron tron")


guitarra = Guitarra()
guitarra.tocar()
guitarra_electrica = GuitarraElectrica()
guitarra_electrica.tocar()
guitarra_electrica.tocar_con_distorsion()
