class Habitat:
    nombre = "Habitat"
    dieta = "Herbívoro"
    tipo = ""
    capacidad = 1
    temperatura = 0
    imagen = "https://www.shutterstock.com/image-vector/default-ui-image-placeholder-wireframes-600w-1037719192.jpg"


    def __init__(self, nombre, dieta, capacidad, temperatura):
        self.nombre = nombre
        self.dieta = dieta
        self.capacidad = capacidad
        self.temperatura = temperatura

    def getImagen(self):
        return self.imagen

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo

    def getDieta(self):
        return self.dieta

    def getCapacidad(self):
        return self.capacidad

    def getTemperatura(self):
        return self.temperatura
