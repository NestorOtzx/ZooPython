class Habitat:

    animales = []


    def __init__(self, nombre, dieta, capacidad, temperatura, extras = {}):
        self.nombre = nombre
        self.dieta = dieta
        self.capacidad = capacidad
        self.temperatura = temperatura
        self.animales = []
        self.extras = extras

        # Valores por defecto
        self.imagen = "https://www.shutterstock.com/image-vector/default-ui-image-placeholder-wireframes-600w-1037719192.jpg"
        self.tipo = "Desértico"


    def getImagen(self):
        return self.imagen

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo

    def getDieta(self):
        return self.dieta

    def getCapacidad(self):
        return self.capacidad

    def getTemperatura(self):
        return self.temperatura

    def agregarAnimal(self, animal):
        self.animales.append(animal)

    def eliminarAnimal(self, animal):
        self.animales.remove(animal)


    def getAnimales(self):
        return self.animales

    # Retorna las características extras de este habitat especifico.
    def getPropiedadesExtra(self):
        return self.extras


    #Función creada para solucionar errores provocados por la funcion __del__(self)
    def destroy(self):
        for x in range(0, len(self.animales)):
            self.animales[x].setHabitat(None)
