import streamlit as st
from streamlit_option_menu import option_menu


def mostrarHabitatsDisponibles(habitats):
    print("animales en cada habitat:")
    for i in range(0, len(habitats)):
        print("-"+habitats[i].getNombre()+"-")
        print(habitats[i].getAnimales())


    if len(habitats) < 1:
        st.subheader("No hay habitats en el zoológico")
    else:
        st.divider()
        print("---MOSTRAR HABITATS--")
        for x in range(0, len(habitats)):
            print("Nueva iteracion "+str(x))
            col1, col2, col3 = st.columns((2,3,2))

            with col1:
                st.image(habitats[x].getImagen())
            with col2:
                st.markdown("### " + habitats[x].getNombre())
                st.markdown("Tipo: " + habitats[x].getTipo())
                st.markdown("Dieta de los animales: " + str(habitats[x].getDieta()))

                propExtras = habitats[x].getPropiedadesExtra()
                for key, valor in propExtras.items():
                    st.write(key + ": "+str(valor))

            with col3:
                #salto de linea
                st.markdown("### \
                &nbsp;")

                st.markdown("Capacidad máxima: " + str(habitats[x].getCapacidad()))
                st.markdown("Temperatura media: " + str(habitats[x].getTemperatura()))

            animales = habitats[x].getAnimales()

            cantidadAnimales=len(animales)
            if len(animales) > 0:
                st.markdown('#### Animales')

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




def mostrarAnimalesDisponibles(animales, habitats):
    if len(animales) < 1:
        st.subheader("No hay animales en el zoológico")
    else:
        st.divider()
        for i in range(0, len(animales)):
            col1, col2, col3 = st.columns((2, 2, 3))

            with col1:
                st.image(animales[i].getImagen())

            with col3:

                if len(habitats) > 0:
                    st.markdown("### Habitats")

                    listaTiposHabitat = ["Ninguno"]
                    for j in range(0, len(habitats)):
                        listaTiposHabitat.append(habitats[j].getNombre())


                    nuevoHabitatIndex = st.selectbox("Asignar habitat", range(len(listaTiposHabitat)),
                                                     format_func=lambda x: listaTiposHabitat[x], key = "selectHabitat"+str(i))

                    if st.button("Asignar nuevo habitat", key="AssHab"+str(i)):

                        if not animales[i].getHabitat() is None:
                            animales[i].getHabitat().eliminarAnimal(animales[i])
                            animales[i].setHabitat(None)

                        if nuevoHabitatIndex == 0:
                            # Asignar que no tiene habitat
                            animales[i].setHabitat(None)
                        else:
                            # asignando habitat nuevo
                            animales[i].setHabitat(habitats[nuevoHabitatIndex - 1])
                            habitats[nuevoHabitatIndex - 1].agregarAnimal(animales[i])

            with col2:
                st.markdown("### " + animales[i].getNombre())
                st.markdown("Especie del animal: "+str(animales[i].getEspecie()))
                st.markdown("Dieta del animal: " + str(animales[i].getDieta()))
                if animales[i].getHabitat() is None:
                    st.write("Habitat: Ninguno")
                else:
                    st.write("Habitat: "+animales[i].getHabitat().getNombre())


            st.divider()


class ZooView:

    mostrandoAgregar = False
    mostrandoEliminar = False
    mostrandoAlimentos = False

    def __init__(self, controller):
        self.controller = controller
        self.configuracionDePagina()
        self.__desactivarLinksEnTitulos__()

    def paginaPrincipal(self):
        with st.sidebar:
            opcion = option_menu(menu_title="Panel de control", options=["Inicio", "Ver Animales", "Configurar Animales", "Ver Habitats", "Configurar Habitats", "Configurar alimentos"],
                                 icons=["border-all", "flower3", "gear", "flower3", "gear", "basket-fill"], menu_icon="display")
        self.controller.seleccionarPagina(opcion)

    def inicio(self):

        col1, col2, col3 = st.columns((1,3,1))

        with col1:
            st.write(' ')

        with col2:
            st.header("Inicio")

            st.markdown(
                "#### Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

            st.image("https://cdn.pixabay.com/photo/2014/08/27/12/58/emperor-penguins-429128_960_720.jpg")

            st.markdown(
                "#### Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

            st.image("https://cdn.pixabay.com/photo/2018/01/30/22/48/rainforest-3119822_960_720.jpg")

            st.markdown(
                "#### Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

            st.image("https://cdn.pixabay.com/photo/2012/03/03/23/54/animal-21668_960_720.jpg")

            st.markdown(
                "#### Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

            st.image("https://cdn.pixabay.com/photo/2019/08/12/20/33/giraffe-4402110_960_720.jpg")

        with col3:
            st.write(' ')
            
    def verAnimales(self, animales):
        st.header("Animales del zoológico")
        mostrarAnimalesDisponibles(animales, [])

    def verHabitats(self, habitats):
        st.header("Habitats del zoológico")
        mostrarHabitatsDisponibles(habitats)

    def configurarAnimales(self, animales, habitats):
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.header("Configuración de animales")

            opcion = option_menu(menu_title="Configurar",
                                 options=["Agregar animal", "Eliminar animal"],
                                 menu_icon="gear")

            if opcion == "Agregar animal":
                with st.form(key="form"):
                    # Nombre
                    nombre = st.text_input('Nombre del animal', 'Nombre')

                    # Especie de animal
                    especie = st.selectbox("Seleccione el tipo de habitat",
                                               ("Jirafa", "Oso polar", "Panda", "Pez payaso", "Pingüino", "Serpiente", "Tiburón", "Tigre"))
                    # Dieta
                    tipoDieta = st.selectbox("Seleccione el tipo de dieta",
                                               ("Herbívoro", "Carnívoro", "Omnívoro"))

                    submit_button = st.form_submit_button(label="Agregar")

                if submit_button:
                    self.controller.agregarAnimal(nombre, especie, tipoDieta)
                else:
                    pass
            elif opcion == "Eliminar animal":
                with st.form(key="form"):
                    listaAnimales = []
                    for x in range(0, len(animales)):
                        listaAnimales.append(animales[x].getNombre())

                    # OBTENER EL INDEX DEL ELEMENTO A ELIMINAR
                    index = st.selectbox("Seleccione el habitat a eliminar", range(len(listaAnimales)), format_func=lambda x: listaAnimales[x])

                    submit_button = st.form_submit_button(label="Eliminar")
                if submit_button:
                    self.controller.eliminarAnimal(index)

                    # recargar la página para actualizar el selectbox
                    st.experimental_rerun()
                    pass
                else:
                    pass

        with col2:
            mostrarAnimalesDisponibles(animales, habitats)

    def configurarHabitats(self, habitats):
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.header("Configuración de habitats")

            opcion = option_menu(menu_title="Configurar",
                                 options=["Agregar Habitats", "Eliminar Habitats"],
                                 menu_icon="gear")

            if opcion == "Agregar Habitats":

                # Tipo
                st.markdown("### Seleccione el tipo de habitat")
                tipoHabitat = st.selectbox("", options = ("Desértico", "Selvático", "Polar", "Acuático"), label_visibility= "hidden")

                with st.form(key="form"):
                    #Nombre
                    nombre = st.text_input('Nombre del habitat', 'Habitat')

                    #Dieta
                    tipoDieta = st.selectbox("Seleccione el tipo de dieta",
                                               ("Herbívoro", "Carnívoro", "Omnívoro"))

                    #Capacidad
                    capacidad = st.slider('¿Cuantos animales podrán vivir en el habitat?', 1, 10, 1)

                    #Temperatura
                    temperatura = st.slider('¿Cual será la temperatura media en grados centígrados del habitat?', -30, 30, 0)

                    # Caracteristicas extra
                    extras = self.caracteristicasEspecificas(tipoHabitat)

                    submit_button = st.form_submit_button(label="Agregar")

                if submit_button:
                    self.controller.agregarHabitat(nombre, tipoHabitat, tipoDieta, capacidad, temperatura, extras)
                else:
                    pass
            elif opcion == "Eliminar Habitats":
                with st.form(key="form"):
                    listaTiposHabitat = []
                    for x in range(0, len(habitats)):
                        listaTiposHabitat.append(habitats[x].getNombre())

                    # OBTENER EL INDEX DEL ELEMENTO A ELIMINAR
                    index = st.selectbox("Seleccione el habitat a eliminar", range(len(listaTiposHabitat)), format_func=lambda x: listaTiposHabitat[x])

                    submit_button = st.form_submit_button(label="Eliminar")
                if submit_button:
                    self.controller.eliminarHabitat(index)
                    # recargar la página para actualizar el selectbox
                    st.experimental_rerun()
                    pass
                else:
                    pass

        with col2:
            mostrarHabitatsDisponibles(habitats)


    def caracteristicasEspecificas(self, tipo):
        extras = {}
        if tipo == 'Desértico':
            extras["Cantidad de cactus"] = st.slider("¿Cuantos cactus tendrá el habitat?", 0, 10)
            hayVegetacion = st.checkbox("¿Hay vegetación en el habitat?")
            extras["Hay vegetación"] = "Si" if hayVegetacion == True else "No"

        elif tipo == 'Selvático':
            extras["Nivel de humedad"] = st.slider("¿Que nivel de humedad tiene el habitat?", 0, 25)
            extras["Cantidad de lianas"] = st.slider("¿Cuantas lianas tendrá el habitat?", 0, 20)

        elif tipo == 'Polar':
            extras["Nivel de humedad"] = st.slider("¿Que nivel de humedad tiene el habitat?", 0, 25)
            hayEstanques = st.checkbox("¿Hay estanques en el habitat?")
            extras["Hay estanques"] = "Si" if hayEstanques == True else "No"

        else:
            # Acuático
            extras["Metros de profundidad"] = st.slider("¿Cuantos metros de profundidad tiene el acuario?", 0, 10)
            extras["Cantidad de corales"] = st.slider("¿Cuantas corales tiene el acuario?", 0, 10)

        return extras

    def crearNuevoHabitat(self):
        seleccion = st.selectbox(
            '¿Qué tipo de habitat desea agregar?',
            ('Desértico', 'Selvático', 'Polar', 'Acuático'))

        self.controller.agregarHabitat(seleccion)
        st.write(seleccion)

    def configurarAlimentos(self):
        st.header("Configuracion de alimentos")


    def __desactivarLinksEnTitulos__(self):
        st.markdown("""
                                <style>
                                .css-15zrgzn {display: none}
                                .css-eczf16 {display: none}
                                .css-jn99sy {display: none}
                                </style>
                                """, unsafe_allow_html=True)

    def configuracionDePagina(self):
        st.set_page_config(
            page_title="Zoológico",
            layout="wide",
            menu_items={
                "About": "https://github.com/NestorOtzx/ZooPython"
            }
        )