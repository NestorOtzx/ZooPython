from Model.Habitat import Habitat
from Model.Animales.Jirafa import Jirafa


class Desertico(Habitat):
    def __init__(self, nombre, dieta, capacidad, temperatura, extras={}):
        Habitat.__init__(self, nombre, dieta, capacidad, temperatura, extras)
        self.tipo = "Desértico"
        self.imagen = "https://cdn.pixabay.com/photo/2020/01/15/03/32/albuca-consanguinea-4766788_960_720.jpg"
