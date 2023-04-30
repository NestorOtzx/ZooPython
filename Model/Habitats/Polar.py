from Model.Habitat import Habitat


class Polar(Habitat):
    def __init__(self, nombre, dieta, capacidad, temperatura, extras={}):
        Habitat.__init__(self, nombre, dieta, capacidad, temperatura, extras)
        self.tipo = "Polar"
        self.imagen = "https://cdn.pixabay.com/photo/2014/08/27/12/59/penguins-429134_960_720.jpg"
