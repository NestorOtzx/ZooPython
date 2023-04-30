from Model.Animal import Animal


class OsoPolar(Animal):

    def __init__(self, nombre, dieta):
        Animal.__init__(self, nombre, dieta)
        self.especie = "Oso polar"
        self.imagen = "https://cdn.pixabay.com/photo/2014/07/29/06/41/polar-bear-404317_960_720.jpg"
