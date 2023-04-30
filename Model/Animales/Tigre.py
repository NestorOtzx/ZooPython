from Model.Animal import Animal


class Tigre(Animal):

    def __init__(self, nombre, dieta):
        Animal.__init__(self, nombre, dieta)
        self.especie = "Tigre"
        self.imagen = "https://cdn.pixabay.com/photo/2013/07/19/00/18/tiger-165189_960_720.jpg"
