from Model.Animal import Animal


class Pinguino(Animal):

    def __init__(self, nombre, dieta, edad=0, estadoSalud="Sano"):
        Animal.__init__(self, nombre, dieta, edad, estadoSalud)
        self.especie = "Pingüino"
        self.fotoNormal = "https://cdn.pixabay.com/photo/2012/09/04/21/20/penguin-56101_960_720.jpg"
        self.fotoComiendo = "https://cdn.pixabay.com/photo/2016/01/23/14/54/penguin-1157508_960_720.jpg"
        self.fotoJugando = "https://cdn.pixabay.com/photo/2013/11/22/23/53/magellanic-penguin-216080_960_720.jpg"
        self.fotoDurmiendo = "https://cdn.pixabay.com/photo/2016/05/11/12/35/penguin-1385647_960_720.jpg"
