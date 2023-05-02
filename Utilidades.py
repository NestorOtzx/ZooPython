class Utilidades:

    @staticmethod
    def obtenerNombreRepetido(lista, nombre):

        #ordenar la lista antes de asignar valor
        lista.sort()


        contador = 0
        nuevoNombre = nombre
        print("-Nombre repetido!!-")
        print(lista)
        print(nombre)
        for x in range(0, len(lista)):
            print("Iteracion "+str(x)+ " nombre actual "+lista[x]+ " == "+nuevoNombre)
            if lista[x] == nuevoNombre:
                print("Es igual!")
                contador += 1
                nuevoNombre = nombre+" "+str(contador)

        print(nuevoNombre)

        return nuevoNombre

