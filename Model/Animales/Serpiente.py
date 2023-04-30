from Model.Animal import Animal


class Serpiente(Animal):

    def __init__(self, nombre, dieta):
        Animal.__init__(self, nombre, dieta)
        self.especie = "Serpiente"
        self.imagen = "https://cdn.pixabay.com/photo/2015/02/28/15/25/speckled-rattlesnake-653642_960_720.jpg"
