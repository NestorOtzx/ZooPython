import streamlit as st
from streamlit_option_menu import option_menu


def mostrarHabitatsDisponibles(habitats):
    if len(habitats) < 1:
        st.subheader("No hay habitats en el zoológico")
    else:
        st.divider()
        for x in range(0, len(habitats)):
            col1, col2, col3 = st.columns((2,3,2))

            with col1:
                st.image(habitats[x].getImagen())
            with col2:
                st.markdown("### " + habitats[x].getNombre())
                st.markdown("Tipo: " + habitats[x].getTipo())
                st.markdown("Dieta de los animales: " + str(habitats[x].getDieta()))

            with col3:
                st.markdown("### \
                &nbsp;")

                st.markdown("Capacidad máxima: " + str(habitats[x].getCapacidad()))
                st.markdown("Temperatura media: " + str(habitats[x].getTemperatura()))
            st.divider()


def mostrarAnimalesDisponibles(animales):
    if len(animales) < 1:
        st.subheader("No hay animales en el zoológico")
    else:
        st.divider()
        for x in range(0, len(animales)):
            col1, col2 = st.columns((1, 3))

            with col1:
                st.image(animales[x].getImagen())
            with col2:
                st.markdown("### " + animales[x].getNombre())
                st.markdown("Dieta del animal: " + str(animales[x].getDieta()))

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
                                 icons=["border-all", "", "", "flower3", "gear", "basket-fill"], menu_icon="display")
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
            
    def verAnimales(self, habitats):
        col1, col2, col3 = st.columns([1, 3, 1])

        with col1:
            st.write(' ')

        with col2:
            if (len(habitats) < 1):
                st.header("No hay animales en el zoológico.")
                return

            st.header("animales en el zoológico")
            listaTiposHabitat = []
            for x in range(0, len(habitats)):
                listaTiposHabitat.append(habitats[x].getNombre())
            index = st.selectbox("Seleccione el habitat a eliminar", range(len(listaTiposHabitat)),
                                 format_func=lambda x: listaTiposHabitat[x])

            st.subheader(habitats[index].getNombre())

        with col3:
            st.write(' ')

    def configurarAnimales(self, animales):
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.header("Configuración de animales")

            opcion = option_menu(menu_title="Configurar",
                                 options=["Agregar animal", "Eliminar animal"],
                                 menu_icon="gear")

            if opcion == "Agregar animal":
                with st.form(key="form"):
                    #Nombre
                    nombre = st.text_input('Nombre del animal', 'Nombre')

                    #Dieta
                    tipoDieta = st.selectbox("Seleccione el tipo de dieta",
                                               ("Herbívoro", "Carnívoro", "Omnívoro"))

                    submit_button = st.form_submit_button(label="Agregar")

                if submit_button:
                    self.controller.agregarAnimal(nombre, tipoDieta)
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
            mostrarAnimalesDisponibles(animales)


    def verHabitats(self, habitats):

        col1, col2, col3 = st.columns([1, 3, 1])

        with col1:
            st.write(' ')

        with col2:
            if (len(habitats) < 1):
                st.header("No hay habitats en el zoológico.")
                return

            st.header("Habitats del zoológico")
            listaTiposHabitat = []
            for x in range(0, len(habitats)):
                listaTiposHabitat.append(habitats[x].getNombre())
            index = st.selectbox("Seleccione el habitat a eliminar", range(len(listaTiposHabitat)),
                                 format_func=lambda x: listaTiposHabitat[x])

            st.subheader(habitats[index].getNombre())

        with col3:
            st.write(' ')

    def configurarHabitats(self, habitats):
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.header("Configuración de habitats")

            opcion = option_menu(menu_title="Configurar",
                                 options=["Agregar Habitats", "Eliminar Habitats"],
                                 menu_icon="gear")

            if opcion == "Agregar Habitats":
                with st.form(key="form"):
                    #Nombre
                    nombre = st.text_input('Nombre del habitat', 'Habitat')

                    #Tipo
                    tipoHabitat = st.selectbox("Seleccione el tipo de habitat", ("Desértico", "Selvático", "Polar", "Acuático"))

                    #Dieta
                    tipoDieta = st.selectbox("Seleccione el tipo de dieta",
                                               ("Herbívoro", "Carnívoro", "Omnívoro"))

                    #Capacidad
                    capacidad = st.slider('¿Cuantos animales podrán vivir en el habitat?', 1, 10, 1)

                    #Temperatura
                    temperatura = st.slider('¿Cual será la temperatura media en grados centígrados del habitat?', -30, 30, 0)

                    submit_button = st.form_submit_button(label="Agregar")

                if submit_button:
                    self.controller.agregarHabitat(nombre, tipoHabitat, tipoDieta, capacidad, temperatura)
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