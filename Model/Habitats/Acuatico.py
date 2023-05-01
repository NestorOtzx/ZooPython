from Model.Habitat import Habitat


class Acuatico(Habitat):
    def __init__(self, nombre, dieta, capacidad, temperatura, extras = {}):
        Habitat.__init__(self, nombre, dieta, capacidad, temperatura, extras)
        self.tipo = "Acuático"
        self.imagen = "https://cdn.pixabay.com/photo/2012/03/03/23/54/animal-21668_960_720.jpg"



