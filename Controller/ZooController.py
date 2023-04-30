from View.ZooView import ZooView
from Model.ZooModel import ZooModel


class ZooController:

    def __init__(self):
        self.view = ZooView(self)
        self.model = ZooModel(self)
        self.mostrarMenuPrincipal()

    def mostrarMenuPrincipal(self):
        self.view.paginaPrincipal()

    def seleccionarPagina(self, pagina):
        self.model.seleccionarPagina(pagina)

    def mostrarInicio(self):
        self.view.inicio()

    def mostrarAnimales(self, animales):
        self.view.verAnimales(animales)

    def mostrarConfAnimales(self, animales, habitats):
        self.view.configurarAnimales(animales, habitats)

    def mostrarHabitats(self, habitats):
        self.view.verHabitats(habitats)

    def mostrarConfHabitats(self, habitats):
        self.view.configurarHabitats(habitats)

    def mostrarConfAlimentos(self):
        self.view.configurarAlimentos()

    def agregarHabitat(self, nombre, tipo, dieta, capacidad, temperatura, listaExtras = {}):
        self.model.agregarHabitat(nombre, tipo, dieta, capacidad, temperatura, listaExtras)

    def agregarAnimal(self, nombre, especie, dieta, edad = 0, estadoDeSalud = "Sano"):
        self.model.agregarAnimal(nombre, especie, dieta, edad, estadoDeSalud)

    def eliminarAnimal(self, id):
        self.model.eliminarAnimal(id)

    def eliminarHabitat(self, id):
        self.model.eliminarHabitat(id)
