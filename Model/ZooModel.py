from Model.Habitats.Polar import Polar
from Model.Habitats.Desertico import Desertico
from Model.Habitats.Acuatico import Acuatico
from Model.Habitats.Selvatico import Selvatico
class ZooModel:
    __habitats__ = []

    def __init__(self, controller):
        self.controller = controller

    def seleccionarPagina(self, pagina):
        if pagina == "Inicio":
            self.controller.mostrarInicio()
        if pagina == "Ver Habitats":
            self.controller.mostarHabitats(self.__habitats__)
        if pagina == "Configurar Habitats":
            self.controller.mostarConfHabitats(self.__habitats__)
        if pagina == "Configurar alimentos":
            self.controller.mostarConfAlimentos()

    def agregarHabitat(self, tipo):


        if tipo == 'Desértico':
            habitat = Desertico(1)

        if tipo == 'Selvático':
            habitat = Selvatico(1)

        if tipo == 'Polar':
            habitat = Polar(1)

        if tipo == 'Acuático':
            habitat = Acuatico(1)

        self.__habitats__.append(habitat)

    def eliminarHabitat(self, id):
        del self.__habitats__[id]


