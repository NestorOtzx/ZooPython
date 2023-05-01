


class Alimento:
    def __init__(self, nombre, tipo, cantidad, imagen):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.imagen = imagen

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo

    def getCantidad(self):
        return self.cantidad

    def getImagen(self):
        return self.imagen

    def destroy(self):
        pass