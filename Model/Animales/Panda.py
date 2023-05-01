from Model.Animal import Animal


class Panda(Animal):

    def __init__(self, nombre, edad=0, estadoSalud="Sano"):
        Animal.__init__(self, nombre, edad, estadoSalud)
        self.especie = "Panda"
        self.fotoNormal = "https://cdn.pixabay.com/photo/2016/03/04/22/54/animal-1236875_960_720.jpg"
        self.fotoComiendo = "https://cdn.pixabay.com/photo/2019/09/08/19/54/panda-4461766_960_720.jpg"
        self.fotoJugando = "https://cdn.pixabay.com/photo/2019/09/15/11/55/panda-4478090_960_720.jpg"
        self.fotoDurmiendo = "https://cdn.pixabay.com/photo/2021/06/13/11/59/panda-6333067_960_720.jpg"

        self.habitatsHabitables = ["Selvático"]

        self.dieta = "Herbívoro"

        self.rangoTemperatura = (10, 25)