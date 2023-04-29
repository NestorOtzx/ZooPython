class Animal:
    nombre = "Nombre"
    dieta = "Herbívoro"
    imagen = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"

    def __init__(self, nombre, dieta):
        self.nombre = nombre
        self.dieta = dieta

    def getNombre(self):
        return self.nombre

    def getDieta(self):
        return self.dieta

    def getImagen(self):
        return self.imagen