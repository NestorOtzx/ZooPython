import streamlit as st
from streamlit_option_menu import option_menu


class ZooView:

    mostrandoAgregar = False
    mostrandoEliminar = False
    mostrandoAlimentos = False


    def __init__(self, controller):
        self.controller = controller
        self.__desactivarLinksEnTitulos__()

    def __desactivarLinksEnTitulos__(self):
        st.markdown("""
                                <style>
                                .css-15zrgzn {display: none}
                                .css-eczf16 {display: none}
                                .css-jn99sy {display: none}
                                </style>
                                """, unsafe_allow_html=True)

    def paginaPrincipal(self):
        with st.sidebar:
            opcion = option_menu(menu_title="Panel de control", options=["Inicio", "Ver Habitats", "Configurar Habitats", "Editar Alimentos"],
                                 icons=["border-all", "flower3", "gear", "egg-fill"], menu_icon="display")
        self.controller.seleccionarPagina(opcion)

    def inicio(self):
        st.header("Inicio")
        st.markdown("#### Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")


    def verHabitats(self, habitats):
        if (len(habitats)< 1):
            st.header("No hay habitats en el zoológico.")
            return

        st.header("Habitats del zoológico")
        listaTiposHabitat = []
        for x in range(0, len(habitats)):
            listaTiposHabitat.append(habitats[x].getNombre())
        index = st.selectbox("Seleccione el habitat a eliminar", range(len(listaTiposHabitat)),
                             format_func=lambda x: listaTiposHabitat[x])

        st.subheader(habitats[index].getNombre())





    def configurarHabitats(self, habitats):
        col1, col2 = st.columns([3, 1], gap="large")
        with col1:
            st.header("Configuración de habitats")

            opcion = option_menu(menu_title="Configurar",
                                 options=["Agregar Habitats", "Eliminar Habitats"],
                                 menu_icon="gear")

            if opcion == "Agregar Habitats":
                with st.form(key="form"):
                    tipoHabitat = st.selectbox("Seleccione el tipo de habitat", ("Desértico", "Selvático", "Polar", "Acuático"))
                    submit_button = st.form_submit_button(label="Agregar")

                if submit_button:
                    self.controller.agregarHabitat(tipoHabitat)
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
            for x in range(0, len(habitats)):
                st.markdown("### " + str(x + 1) + " " + habitats[x].getNombre())


    def crearNuevoHabitat(self):
        seleccion = st.selectbox(
            '¿Qué tipo de habitat desea agregar?',
            ('Desértico', 'Selvático', 'Polar', 'Acuático'))

        self.controller.agregarHabitat(seleccion)
        st.write(seleccion)




    def configurarAlimentos(self):
        st.header("Configuracion de alimentos")
