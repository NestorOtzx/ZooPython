from Model.Habitat import Habitat


class Selvatico(Habitat):

    def __init__(self, temperatura):
        Habitat.__init__(self, temperatura)
        self.nombre = "Selvatico"
