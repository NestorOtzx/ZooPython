from View.ZooView import ZooView
from View.HabitatsView import HabitatsView
from View.AnimalesView import AnimalesView
from View.AlimentosView import AlimentosView
from View.InicioView import InicioView


from Model.ZooModel import ZooModel


class ZooController:

    def __init__(self):
        self.zooView = ZooView(self)
        self.habitatsView = HabitatsView(self)
        self.animalesView = AnimalesView(self)
        self.alimentosView = AlimentosView(self)
        self.inicioView = InicioView(self)

        self.model = ZooModel(self)
        self.mostrarMenuPrincipal()

    def mostrarMenuPrincipal(self):
        self.zooView.paginaPrincipal()

    def seleccionarPagina(self, pagina):
        self.model.seleccionarPagina(pagina)

    def mostrarInicio(self):
        self.inicioView.inicio()

    def mostrarAnimales(self, animales, alimentos = []):
        self.animalesView.verAnimales(animales, alimentos)

    def mostrarConfAnimales(self, animales, habitats):
        self.animalesView.configurarAnimales(animales, habitats)

    def mostrarHabitats(self, habitats):
        self.habitatsView.verHabitats(habitats)

    def mostrarConfHabitats(self, habitats):
        self.habitatsView.configurarHabitats(habitats)

    def mostrarAlimentos(self, alimentos):
        self.alimentosView.mostrarAlimentos(alimentos)

    def mostrarConfAlimentos(self, alimentos):
        self.alimentosView.configurarAlimentos(alimentos)

    def agregarHabitat(self, nombre, tipo, dieta, capacidad, temperatura, listaExtras = {}):
        self.model.agregarHabitat(nombre, tipo, dieta, capacidad, temperatura, listaExtras)

    def agregarAnimal(self, nombre, especie, edad = 0, estadoDeSalud = "Sano"):
        self.model.agregarAnimal(nombre, especie, edad, estadoDeSalud)

    def agregarAlimento(self, nombre, tipo, cantidad, imagen):
        self.model.agregarAlimento(nombre, tipo, cantidad, imagen)

    def eliminarAnimal(self, id):
        self.model.eliminarAnimal(id)

    def eliminarHabitat(self, id):
        self.model.eliminarHabitat(id)

    def eliminarAlimento(self, id):
        self.model.eliminarAlimento(id)
