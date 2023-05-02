


class Alimento:
    def __init__(self, nombre, tipo, cantidad, imagen):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad

        # Icono generado de manera aleatoria que depende del tipo de alimento.
        self.imagen = imagen

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo

    def getCantidad(self):
        return self.cantidad

    def getImagen(self):
        return self.imagen

    def reducirCantidad(self):
        self.cantidad -= 1

    def editarAlimento(self, nombre = "", tipo = "", cantidad = -1, imagen = ""):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.imagen = imagen

    def destroy(self):
        del self