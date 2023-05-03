import streamlit as st
import requests



class InicioView:
    def __init__(self, controller):
        self.controller = controller

    def inicio(self):



        col1, col2, col3 = st.columns((1,5,1))

        with col1:
            st.write(' ')

        with col2:
            st.header("Inicio")
            st.subheader("¡Datos importantes sobre nuestros animales!")

            animales = {"giraffe":"https://cdn.pixabay.com/photo/2018/04/23/14/23/giraffe-3344366_960_720.jpg",
                        "Polar bear":"https://cdn.pixabay.com/photo/2014/07/29/06/41/polar-bear-404317_960_720.jpg",
                        "Panda":"https://cdn.pixabay.com/photo/2016/03/04/22/54/animal-1236875_960_720.jpg",
                        "Clownfish":"https://cdn.pixabay.com/photo/2016/07/04/16/05/anemone-fish-1496866_960_720.jpg",
                        "Penguin":"https://cdn.pixabay.com/photo/2012/09/04/21/20/penguin-56101_960_720.jpg",
                        "Snake":"https://cdn.pixabay.com/photo/2015/02/28/15/25/speckled-rattlesnake-653642_960_720.jpg",
                        "Shark":"https://cdn.pixabay.com/photo/2019/12/30/12/28/shark-4729554_960_720.jpg",
                        "Tiger":"https://cdn.pixabay.com/photo/2013/07/19/00/18/tiger-165189_960_720.jpg"}

            st.divider()
            for nombre, foto in animales.items():
                datos = self.getDatos(nombre)
                self.mostrarAnimal(foto, datos)

        with col3:
            st.write(' ')

    def mostrarAnimal(self, foto, datos):
        col1, col2 = st.columns(2)

        with col1:
            st.image(foto)
        with col2:
            for key, val in datos.items():
                st.markdown("**"+key + "**: " + val)
        st.divider()
    # Obtiene datos curiosos de una api de animales
    def getDatos(self, animal):
        api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal)
        response = requests.get(api_url, headers={'X-Api-Key': 'paY1BtYA/zM/Ct/3GtOGOA==A6zb4QkNADxPrNxf'})

        datosImportantes = {}

        if response.status_code == 200:
            res = response.json()
            dict = res[0]

            if dict.get("name"):
                datosImportantes["Nombre"] = dict["name"]

            if dict["taxonomy"].get("scientific_name"):
                datosImportantes["Nombre científico"] = dict["taxonomy"]["scientific_name"]

            if dict["characteristics"].get("diet"):
                datosImportantes["Alimentación"] = dict["characteristics"]["diet"]

            if dict["characteristics"].get("weight"):
                datosImportantes["Peso"] = dict["characteristics"]["weight"]

            if dict["characteristics"].get("length"):
                datosImportantes["Tamaño"] = dict["characteristics"]["length"]

            if dict["characteristics"].get("top_speed"):
                datosImportantes["Velocidad máxima"] = dict["characteristics"]["top_speed"]

            if dict["characteristics"].get("location"):
                datosImportantes["Ubicación"] = dict["characteristics"]["location"]

            if dict["characteristics"].get("prey"):
                datosImportantes["Alimento"] = dict["characteristics"]["prey"]

            if dict.get("locations"):
                ubicaciones = ""
                contador = 0
                for x in dict["locations"]:
                    if contador == 0:
                        ubicaciones += x
                    else:
                        ubicaciones += ", "+x
                    contador += 1

                if len(ubicaciones)>0:
                    datosImportantes["Dónde se encuentra"] = ubicaciones


        else:
            st.error("Error: " + str(response.status_code))
            pass

        return datosImportantes
