
class Animal:
    nombre = "Animal"
    dieta = "Omnívoro"
    especie = "Especie"

    edad = 0

    estadoDeSalud = "Sano"
    habitat = None

    MAX_HORAS_SUENIO = 8
    horasSuenio = 0

    jugoEnElDia = False

    habitatsHabitables = []

    rangoTemperatura = (-100, 100)


    def __init__(self, nombre, edad = 0, estadoSalud = "Sano"):
        self.nombre = nombre
        self.estadoDeSalud = estadoSalud
        self.edad = edad
        self.habitat = None

        # Fotos de cada acción ejecutable por el animal
        self.fotoNormal = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"
        self.fotoComiendo = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"
        self.fotoJugando = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"
        self.fotoDurmiendo = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"

        self.jugoEnElDia = False

        self.durmioSuficiente = False

        # Lista de habitats en los que el animal puede vivir, por defecto, puede vivir en todos.
        self.habitatsHabitables = ["Acuático", "Desértico", "Polar", "Selvático"]

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

        # En caso de que el animal no contenga ninguna foto para la acción requerida,
        # se asume que el animal no puede realizar dicha acción.
        if foto == "":
            raise ValueError("El "+ self.especie+" no puede "+accion)

        return foto

    # Comprueba si la acción es posible de realizar por el animal, si no, arroja una excepción.
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
            if not self.dieta == "Omnívoro" and self.dieta != parametro.getTipo():
                raise Exception("El animal es "+self.dieta+ " y no puede comer alimentos del tipo "+parametro.getTipo())



    def getHabitat(self):
        return self.habitat

    # Comprueba si el animal puede habitar en el hábitat dado, si no, arroja una excepción.
    def setHabitat(self, habitat):
        # Comprobar habitat
        if habitat is None:
            self.habitat = None
            return

        if not habitat.getTipo() in self.habitatsHabitables:
            raise Exception("La especie "+self.especie+ " no puede habitar en el habitat "+habitat.getTipo())

        # Comprobar temperatura
        if self.rangoTemperatura[0]> habitat.getTemperatura():
            raise Exception("El animal "+self.especie+" no puede vivir en temperaturas inferiores a "+str(self.rangoTemperatura[0])+"°C")
        if self.rangoTemperatura[1]< habitat.getTemperatura():
            raise Exception("El animal "+self.especie+" no puede vivir en temperaturas superiores a "+str(self.rangoTemperatura[1])+"°C")


        # Comprobar capacidad
        if len(habitat.getAnimales()) >= habitat.getCapacidad():
            raise Exception("No caben más animales en el zoológico")


        # Comprobar dieta
        if (habitat.getDieta() == "Omnívoro") or (habitat.getDieta() == self.dieta):
            self.habitat = habitat
        else:
            raise Exception("La dieta del animal (" + self.dieta + ") no coincide con la dieta asignada al habitat (" + habitat.getDieta() + ")")




    def getSalud(self):
        return self.estadoDeSalud

    def getEdad(self):
        return self.edad

    def getTemperatura(self):
        return self.rangoTemperatura

    # Función creada para solucionar errores provocados por la funcion __del__(self)
    def destroy(self):
        if not self.habitat is None:
            self.habitat.eliminarAnimal(self)
