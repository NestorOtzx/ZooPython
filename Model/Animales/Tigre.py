from Model.Animal import Animal


class Tigre(Animal):

    def __init__(self, nombre, edad=0, estadoSalud="Sano"):
        Animal.__init__(self, nombre, edad, estadoSalud)
        self.especie = "Tigre"
        self.fotoNormal = "https://cdn.pixabay.com/photo/2013/07/19/00/18/tiger-165189_960_720.jpg"
        self.fotoComiendo = "https://cdn.pixabay.com/photo/2019/08/25/12/11/tiger-4429338_960_720.jpg"
        self.fotoJugando = "https://cdn.pixabay.com/photo/2016/07/21/02/20/tiger-1531731_960_720.jpg"
        self.fotoDurmiendo = "https://cdn.pixabay.com/photo/2017/07/22/22/56/tiger-2530158_960_720.jpg"

        self.habitatsHabitables = ["Desértico", "Selvático"]

        self.dieta = "Carnívoro"

        self.rangoTemperatura = (10, 40)
