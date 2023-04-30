
class Animal:
    nombre = "Animal"
    dieta = "Herbívoro"
    imagen = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"
    especie = "Especie"
    habitat = None

    def __init__(self, nombre, dieta):
        self.nombre = nombre
        self.dieta = dieta

    def getNombre(self):
        return self.nombre

    def getEspecie(self):
        return self.especie

    def getDieta(self):
        return self.dieta

    def getImagen(self):
        return self.imagen

    def getHabitat(self):
        return self.habitat

    def setHabitat(self, habitat):
        self.habitat = habitat

    def __del__(self):
        if not self.habitat is None:
            self.habitat.eliminarAnimal(self)
