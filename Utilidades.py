class Utilidades:

    @staticmethod
    def obtenerNombreRepetido(lista, nombre):
        contador = 0
        nuevoNombre = nombre
        for x in range(0, len(lista)):
            if lista[x] == nuevoNombre:
                contador += 1
                nuevoNombre = nombre+" "+str(contador)

        return nuevoNombre
