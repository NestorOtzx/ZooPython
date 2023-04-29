from Model.Habitat import Habitat


class Selvatico(Habitat):

    def __init__(self, nombre, dieta, capacidad, temperatura):
        Habitat.__init__(self, nombre, dieta, capacidad, temperatura)
        self.tipo = "Selvático"
        self.imagen = "https://cdn.pixabay.com/photo/2019/07/20/14/29/rainforest-4350845_960_720.jpg"
