class Habitat:

    nombre = "Habitat"
    __temperatura__ = 0

    def __init__(self, temperatura):
        self.__temperatura__ = temperatura

    def getNombre(self):
        return self.nombre

    def getTemperatura(self):
        return self.__temperatura__
