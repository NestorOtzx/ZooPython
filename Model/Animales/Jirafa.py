from Model.Animal import Animal


class Jirafa(Animal):

    def __init__(self, nombre, dieta):
        Animal.__init__(self, nombre, dieta)
        self.especie = "Jirafa"
        self.imagen = "https://cdn.pixabay.com/photo/2018/04/23/14/23/giraffe-3344366_960_720.jpg"
