from Model.Habitats.Polar import Polar
from Model.Habitats.Desertico import Desertico
from Model.Habitats.Acuatico import Acuatico
from Model.Habitats.Selvatico import Selvatico
from Model.Animales.Jirafa import Jirafa
from Model.Animales.OsoPolar import OsoPolar
from Model.Animales.Panda import Panda
from Model.Animales.PezPayaso import PezPayaso
from Model.Animales.Pinguino import Pinguino
from Model.Animales.Serpiente import Serpiente
from Model.Animales.Tiburon import Tiburon
from Model.Animales.Tigre import Tigre
from Model.Alimento import Alimento

class ZooModel:
    __habitats__ = []
    __animales__ = []
    __alimentos__ = []

    def __init__(self, controller):
        self.controller = controller

    def seleccionarPagina(self, pagina):
        if pagina == "Inicio":
            self.controller.mostrarInicio()
        if pagina == "Ver Animales":
            self.controller.mostrarAnimales(self.__animales__, self.__alimentos__)
        if pagina == "Configurar Animales":
            self.controller.mostrarConfAnimales(self.__animales__, self.__habitats__)
        if pagina == "Ver Habitats":
            self.controller.mostrarHabitats(self.__habitats__)
        if pagina == "Configurar Habitats":
            self.controller.mostrarConfHabitats(self.__habitats__)
        if pagina == "Ver Alimentos":
            self.controller.mostrarAlimentos(self.__alimentos__)
        if pagina == "Configurar alimentos":
            self.controller.mostrarConfAlimentos(self.__alimentos__)

    def agregarHabitat(self, nombre, tipo, dieta, capacidad, temperatura, extras = {}):

        if tipo == 'Desértico':
            habitat = Desertico(nombre, dieta, capacidad, temperatura, extras)

        elif tipo == 'Selvático':
            habitat = Selvatico(nombre, dieta, capacidad, temperatura, extras)

        elif tipo == 'Polar':
            habitat = Polar(nombre, dieta, capacidad, temperatura, extras)
        else:
            # Acuático
            habitat = Acuatico(nombre, dieta, capacidad, temperatura, extras)

        self.__habitats__.append(habitat)

    def agregarAnimal(self, nombre, especie, edad = 0, estadoDeSalud = "Sano"):
        animal = None

        if especie == "Jirafa":
            animal = Jirafa(nombre, edad, estadoDeSalud)
        if especie == "Oso polar":
            animal = OsoPolar(nombre, edad, estadoDeSalud)
        if especie == "Panda":
            animal = Panda(nombre, edad, estadoDeSalud)
        if especie == "Pez payaso":
            animal = PezPayaso(nombre, edad, estadoDeSalud)
        if especie == "Pingüino":
            animal = Pinguino(nombre, edad, estadoDeSalud)
        if especie == "Serpiente":
            animal = Serpiente(nombre, edad, estadoDeSalud)
        if especie == "Tiburón":
            animal = Tiburon(nombre, edad, estadoDeSalud)
        if especie == "Tigre":
            animal = Tigre(nombre, edad, estadoDeSalud)

        self.__animales__.append(animal)

    def agregarAlimento(self, nombre, tipo, cantidad, imagen):
        self.__alimentos__.append(Alimento(nombre, tipo, cantidad, imagen))

    def eliminarAlimento(self, id):
        self.__alimentos__[id].destroy()
        del self.__alimentos__[id]

    def eliminarHabitat(self, id):
        self.__habitats__[id].destroy()
        del self.__habitats__[id]

    def eliminarAnimal(self, id):
        self.__animales__[id].destroy()
        del self.__animales__[id]

