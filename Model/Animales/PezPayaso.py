from Model.Animal import Animal


class PezPayaso(Animal):

    def __init__(self, nombre, dieta):
        Animal.__init__(self, nombre, dieta)
        self.especie = "Pez payaso"
        self.imagen = "https://cdn.pixabay.com/photo/2016/07/04/16/05/anemone-fish-1496866_960_720.jpg"
