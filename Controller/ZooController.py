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

    def mostarHabitats(self, habitats):
        self.view.verHabitats(habitats)

    def mostarConfHabitats(self, habitats):
        self.view.configurarHabitats(habitats)

    def mostarConfAlimentos(self):
        self.view.configurarAlimentos()

    def agregarHabitat(self, tipo):
        self.model.agregarHabitat(tipo)

    def eliminarHabitat(self, id):
        self.model.eliminarHabitat(id)
