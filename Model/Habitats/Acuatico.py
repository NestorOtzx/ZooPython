from Model.Habitat import Habitat


class Acuatico(Habitat):

    def __init__(self, temperatura):
        Habitat.__init__(self, temperatura)
        self.nombre = "Acuatico"

