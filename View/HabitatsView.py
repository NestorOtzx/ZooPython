import streamlit as st
from streamlit_option_menu import option_menu
from Utilidades import Utilidades

class HabitatsView:
    # Características de habitats
    MAX_CACTUS = 10
    MAX_HUMEDAD = 25
    MAX_LIANAS = 20
    MAX_ROCAS = 25
    MAX_PROFUNDIDAD = 10
    MAX_CORALES = 10

    def __init__(self, controller):
        self.controller = controller

    def verHabitats(self, habitats):
        st.header("Habitats del zoológico")
        self.mostrarHabitatsDisponibles(habitats)

    # Recibe una lista de habitats que se encarga de mostrar,
    # junto con las características de cada uno de ellos.
    def mostrarHabitatsDisponibles(self, habitats):

        if len(habitats) < 1:
            st.subheader("No hay habitats en el zoológico")
        else:
            st.divider()
            for x in range(0, len(habitats)):
                col1, col2, col3 = st.columns((2, 3, 2))

                with col1:
                    st.image(habitats[x].getImagen())
                with col2:
                    st.markdown("### " + habitats[x].getNombre())
                    st.markdown("Tipo: " + habitats[x].getTipo())
                    st.markdown("Dieta de los animales: " + str(habitats[x].getDieta()))

                    propExtras = habitats[x].getPropiedadesExtra()
                    for key, valor in propExtras.items():
                        st.write(key + ": " + str(valor))

                with col3:
                    # salto de linea
                    st.markdown("### \
                    &nbsp;")

                    st.markdown("Capacidad máxima: " + str(habitats[x].getCapacidad()))
                    st.markdown("Temperatura media: " + str(habitats[x].getTemperatura()) + "°C")

                animales = habitats[x].getAnimales()

                cantidadAnimales = len(animales)
                if len(animales) > 0:
                    st.markdown('#### Animales ' + str(cantidadAnimales) + "/" + str(habitats[x].getCapacidad()))

                    columnas = 8
                    cols = st.columns(columnas)

                    i = 0
                    colActual = 0

                    while i < cantidadAnimales:
                        if colActual >= columnas:
                            colActual = 0

                        cols[colActual].image(animales[i].getImagen())
                        cols[colActual].write(animales[i].getNombre())

                        colActual += 1
                        i += 1

                st.divider()

    # Permite crear y eliminar habitats en el zoológico, cada tipo de habitat con sus respectivas características
    def configurarHabitats(self, habitats):
        col1, col2 = st.columns(2, gap="large")

        listaNombresHabitat = []
        for x in range(0, len(habitats)):
            listaNombresHabitat.append(habitats[x].getNombre())

        with col1:
            st.header("Configuración de habitats")

            opcion = option_menu(menu_title="Configurar",
                                 options=["Agregar Habitats", "Eliminar Habitats"],
                                 menu_icon="gear")

            if opcion == "Agregar Habitats":

                # Tipo
                st.markdown("### Seleccione el tipo de habitat")
                tipoHabitat = st.selectbox("Tipo de hábitat", options = ("Desértico", "Selvático", "Polar", "Acuático"))

                with st.form(key="form"):
                    #Nombre
                    nombre = st.text_input('Nombre del habitat', 'Habitat')

                    #Dieta
                    tipoDieta = st.selectbox("Seleccione el tipo de dieta",
                                               ("Herbívoro", "Carnívoro", "Omnívoro"))

                    #Capacidad
                    capacidad = st.slider('¿Cuantos animales podrán vivir en el habitat?', 1, 10, 1)

                    #Temperatura
                    temperatura = st.slider('¿Cual será la temperatura media en °C del habitat?', -40, 40, 15)

                    # Caracteristicas extra
                    extras = self.caracteristicasEspecificas(tipoHabitat)

                    submit_button = st.form_submit_button(label="Agregar")

                if submit_button:
                    self.controller.agregarHabitat(Utilidades.obtenerNombreRepetido(listaNombresHabitat, nombre), tipoHabitat, tipoDieta, capacidad, temperatura, extras)
                else:
                    pass
            elif opcion == "Eliminar Habitats":
                with st.form(key="form"):


                    # OBTENER EL INDEX DEL ELEMENTO A ELIMINAR
                    index = st.selectbox("Seleccione el habitat a eliminar", range(len(listaNombresHabitat)), format_func=lambda x: listaNombresHabitat[x])

                    submit_button = st.form_submit_button(label="Eliminar")
                if submit_button:
                    self.controller.eliminarHabitat(index)
                    # recargar la página para actualizar el selectbox
                    st.experimental_rerun()
                    pass
                else:
                    pass

        with col2:
            self.mostrarHabitatsDisponibles(habitats)

    def caracteristicasEspecificas(self, tipo):
        extras = {}



        if tipo == 'Desértico':
            extras["Cantidad de cactus"] = st.slider("¿Cuantos cactus tendrá el habitat?", 0, self.MAX_CACTUS)
            hayVegetacion = st.checkbox("¿Hay vegetación en el habitat?")
            extras["Hay vegetación"] = "Si" if hayVegetacion == True else "No"

        elif tipo == 'Selvático':
            extras["Nivel de humedad"] = st.slider("¿Que nivel de humedad tiene el habitat?", 0, self.MAX_HUMEDAD)
            extras["Cantidad de lianas"] = st.slider("¿Cuantas lianas tendrá el habitat?", 0, self.MAX_LIANAS)

        elif tipo == 'Polar':
            extras["Cantidad de rocas"] = st.slider("¿Cuantas rocas tendrá el habitat?", 0, self.MAX_ROCAS)
            hayEstanques = st.checkbox("¿Hay estanques en el habitat?")
            extras["Hay estanques"] = "Si" if hayEstanques == True else "No"

        else:
            # Acuático
            extras["Metros de profundidad"] = st.slider("¿Cuantos metros de profundidad tiene el acuario?", 0, self.MAX_PROFUNDIDAD)
            extras["Cantidad de corales"] = st.slider("¿Cuantas corales tiene el acuario?", 0, self.MAX_CORALES)

        return extras