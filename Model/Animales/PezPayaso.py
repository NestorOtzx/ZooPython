from Model.Animal import Animal


class PezPayaso(Animal):

    def __init__(self, nombre, dieta, edad=0, estadoSalud="Sano"):
        Animal.__init__(self, nombre, dieta, edad, estadoSalud)
        self.especie = "Pez payaso"
        self.fotoNormal = "https://cdn.pixabay.com/photo/2016/07/04/16/05/anemone-fish-1496866_960_720.jpg"
        self.fotoComiendo = "https://cdn.pixabay.com/photo/2014/04/12/13/55/clown-fish-322419_960_720.jpg"
        self.fotoJugando = ""
        self.fotoDurmiendo = "https://cdn.pixabay.com/photo/2013/12/09/03/44/clown-fish-225421_960_720.jpg"
