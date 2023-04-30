from Model.Animal import Animal


class Serpiente(Animal):

    def __init__(self, nombre, dieta, edad=0, estadoSalud="Sano"):
        Animal.__init__(self, nombre, dieta, edad, estadoSalud)
        self.especie = "Serpiente"
        self.fotoNormal = "https://cdn.pixabay.com/photo/2015/02/28/15/25/speckled-rattlesnake-653642_960_720.jpg"
        self.fotoComiendo = "https://cdn.pixabay.com/photo/2020/01/11/09/57/carpet-python-4757065_960_720.jpg"
        self.fotoJugando = ""
        self.fotoDurmiendo = ""
