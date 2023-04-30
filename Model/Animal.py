
class Animal:
    nombre = "Animal"
    dieta = "Herbívoro"
    especie = "Especie"
    edad = 0
    estadoDeSalud = "Sano"
    habitat = None

    MAX_HORAS_SUENIO = 8
    horasSuenio = 0

    jugoEnElDia = False



    def __init__(self, nombre, dieta, edad = 0, estadoSalud = "Sano"):
        self.nombre = nombre
        self.dieta = dieta
        self.estadoDeSalud = estadoSalud
        self.edad = edad
        self.habitat = None

        self.fotoNormal = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"
        self.fotoComiendo = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"
        self.fotoJugando = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"
        self.fotoDurmiendo = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"

        self.jugoEnElDia = False

        self.durmioSuficiente = False

    def getNombre(self):
        return self.nombre

    def getEspecie(self):
        return self.especie

    def getDieta(self):
        return self.dieta

    def getImagen(self, accion = "Nada"):
        foto = ""
        if accion == "Nada":
            foto = self.fotoNormal
        if accion == "Jugar":
            foto = self.fotoJugando
        if accion == "Dormir":
            foto = self.fotoDurmiendo
        if accion == "Comer":
            foto = self.fotoComiendo

        #arrojar excepcion
        if foto == "":
            raise ValueError("El "+ self.especie+" no puede "+accion)

        return foto

    def ejecutarAccion(self, accion, parametro = None):
        if accion == "Jugar":
            if self.jugoEnElDia:
                raise Exception("El animal ya jugo suficiente por hoy")
            else:
                self.jugoEnElDia = True
            pass
        if accion == "Dormir":
            if self.horasSuenio >= self.MAX_HORAS_SUENIO:
                raise Exception("El animal ya durmio suficiente")
            else:
                self.horasSuenio += int(parametro)
        if accion == "Comer":
            pass



    def getHabitat(self):
        return self.habitat

    def setHabitat(self, habitat):
        self.habitat = habitat

    def getSalud(self):
        return self.estadoDeSalud

    def getEdad(self):
        return self.edad

    def __del__(self):
        if not self.habitat is None:
            self.habitat.eliminarAnimal(self)
