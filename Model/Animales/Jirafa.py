from Model.Animal import Animal


class Jirafa(Animal):

    def __init__(self, nombre, edad = 0, estadoSalud = "Sano"):
        Animal.__init__(self, nombre, edad, estadoSalud)

        self.especie = "Jirafa"

        # Fotos de cada acción ejecutable por el animal
        self.fotoNormal = "https://cdn.pixabay.com/photo/2018/04/23/14/23/giraffe-3344366_960_720.jpg"
        self.fotoComiendo = "https://cdn.pixabay.com/photo/2017/10/20/14/51/giraffe-2871412_960_720.jpg"
        self.fotoJugando = "https://cdn.pixabay.com/photo/2019/05/03/22/58/giraffe-4177095_960_720.jpg"
        self.fotoDurmiendo = "https://cdn.pixabay.com/photo/2016/02/05/03/16/giraffe-1180300_960_720.jpg"

        # Lista de los tipos de habitat en los que puede vivir el animal
        self.habitatsHabitables = ["Desértico", "Selvático"]

        self.dieta = "Herbívoro"

        self.rangoTemperatura = (15, 40)

