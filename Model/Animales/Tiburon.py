from Model.Animal import Animal


class Tiburon(Animal):

    def __init__(self, nombre, edad=0, estadoSalud="Sano"):
        Animal.__init__(self, nombre, edad, estadoSalud)

        self.especie = "Tiburón"

        # Fotos de cada acción ejecutable por el animal
        self.fotoNormal = "https://cdn.pixabay.com/photo/2019/12/30/12/28/shark-4729554_960_720.jpg"
        self.fotoComiendo = "https://cdn.pixabay.com/photo/2015/03/15/19/05/shark-674867_960_720.jpg"
        self.fotoJugando = ""
        self.fotoDurmiendo = ""

        # Lista de los tipos de habitat en los que puede vivir el animal
        self.habitatsHabitables = ["Acuático"]

        self.dieta = "Carnívoro"

        self.rangoTemperatura = (10, 30)
