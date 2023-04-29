from Model.Habitats.Polar import Polar
from Model.Habitats.Desertico import Desertico
from Model.Habitats.Acuatico import Acuatico
from Model.Habitats.Selvatico import Selvatico
from Model.Animal import Animal

class ZooModel:
    __habitats__ = []
    __animales__ = []

    def __init__(self, controller):
        self.controller = controller

    def seleccionarPagina(self, pagina):
        if pagina == "Inicio":
            self.controller.mostrarInicio()
        if pagina == "Ver Animales":
            self.controller.mostrarAnimales(self.__animales__)
        if pagina == "Configurar Animales":
            self.controller.mostrarConfAnimales(self.__animales__)
        if pagina == "Ver Habitats":
            self.controller.mostrarHabitats(self.__habitats__)
        if pagina == "Configurar Habitats":
            self.controller.mostrarConfHabitats(self.__habitats__)
        if pagina == "Configurar alimentos":
            self.controller.mostrarConfAlimentos()

    def agregarHabitat(self, nombre, tipo, dieta, capacidad, temperatura):

        if tipo == 'Desértico':
            habitat = Desertico(nombre, dieta, capacidad, temperatura)

        elif tipo == 'Selvático':
            habitat = Selvatico(nombre, dieta, capacidad, temperatura)

        elif tipo == 'Polar':
            habitat = Polar(nombre, dieta, capacidad, temperatura)
        else:
            # Acuático
            habitat = Acuatico(nombre, dieta, capacidad, temperatura)

        self.__habitats__.append(habitat)

    def agregarAnimal(self, nombre, dieta):
        animal = Animal(nombre, dieta)
        self.__animales__.append(animal)

    def eliminarHabitat(self, id):
        del self.__habitats__[id]

    def eliminarAnimal(self, id):
        del self.__animales__[id]

