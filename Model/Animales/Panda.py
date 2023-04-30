from Model.Animal import Animal


class Panda(Animal):

    def __init__(self, nombre, dieta):
        Animal.__init__(self, nombre, dieta)
        self.especie = "Panda"
        self.imagen = "https://cdn.pixabay.com/photo/2016/03/04/22/54/animal-1236875_960_720.jpg"
