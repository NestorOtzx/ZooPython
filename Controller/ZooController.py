from Model.ZooModel import ZooModel
from View.ZooView import ZooView
class ZooController:

    def __init__(self):
        self.view = ZooView()

    def MostrarAnimales(self):
        self.view.MostrarAnimales()
