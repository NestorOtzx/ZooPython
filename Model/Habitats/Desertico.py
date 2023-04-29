from Model.Habitat import Habitat


class Desertico(Habitat):

    def __init__(self, nombre, dieta, capacidad, temperatura):
        Habitat.__init__(self, nombre, dieta, capacidad, temperatura)
        self.tipo = "Desértico"
        self.imagen = "https://cdn.pixabay.com/photo/2017/08/29/03/33/girafe-2692014_960_720.jpg"
