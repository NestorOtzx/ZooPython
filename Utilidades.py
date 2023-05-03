class Utilidades:

    @staticmethod
    def obtenerNombreRepetido(lista, nombre):

        #ordenar la lista antes de asignar valor
        lista.sort()

        contador = 0
        nuevoNombre = nombre
        for x in range(0, len(lista)):
            if lista[x] == nuevoNombre:
                contador += 1
                nuevoNombre = nombre+" "+str(contador)

        print(nuevoNombre)

        return nuevoNombre

