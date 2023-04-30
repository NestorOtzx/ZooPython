from Model.Animal import Animal


class Pinguino(Animal):

    def __init__(self, nombre, dieta):
        Animal.__init__(self, nombre, dieta)
        self.especie = "Pingüino"
        self.imagen = "https://cdn.pixabay.com/photo/2012/09/04/21/20/penguin-56101_960_720.jpg"
