from Model.Animal import Animal


class Tiburon(Animal):

    def __init__(self, nombre, dieta):
        Animal.__init__(self, nombre, dieta)
        self.especie = "Tiburón"
        self.imagen = "https://cdn.pixabay.com/photo/2019/12/30/12/28/shark-4729554_960_720.jpg"
