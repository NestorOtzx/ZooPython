from Model.Animal import Animal


class OsoPolar(Animal):

    def __init__(self, nombre, dieta, edad=0, estadoSalud="Sano"):
        Animal.__init__(self, nombre, dieta, edad, estadoSalud)
        self.especie = "Oso polar"
        self.fotoNormal = "https://cdn.pixabay.com/photo/2014/07/29/06/41/polar-bear-404317_960_720.jpg"
        self.fotoComiendo = "https://cdn.pixabay.com/photo/2016/10/01/10/28/polar-bear-1707199_960_720.jpg"
        self.fotoJugando = "https://cdn.pixabay.com/photo/2014/09/12/19/12/polar-bear-443203_960_720.jpg"
        self.fotoDurmiendo = "https://cdn.pixabay.com/photo/2022/08/10/20/17/polar-bear-7378112_960_720.jpg"
