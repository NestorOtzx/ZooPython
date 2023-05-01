import streamlit as st
from streamlit_option_menu import option_menu


class AlimentosView:

    def __init__(self, controller):
        self.controller = controller

    def mostrarAlimentos(self, alimentos):
        pass

    def configurarAlimentos(self, alimentos):

        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.header("Configuración de alimentos")

            opcion = option_menu(menu_title="Configurar",
                                 options=["Agregar alimentos", "Editar alimentos", "Eliminar alimentos"],
                                 menu_icon="gear")

            if opcion == "Agregar alimentos":

                # Tipo
                st.markdown("### Seleccione el tipo de alimento")
                tipoHabitat = st.selectbox("Tipo de alimento", options=("Carnívoro", "Herbívoro"))

                with st.form(key="form"):
                    # Nombre
                    nombre = st.text_input('Nombre del alimento', 'Habitat')

                    # Dieta
                    tipoDieta = st.selectbox("Seleccione el tipo de dieta",
                                             ("Herbívoro", "Carnívoro", "Omnívoro"))


                    submit_button = st.form_submit_button(label="Agregar")

                if submit_button:
                    pass
                else:
                    pass
            elif opcion == "Editar alimentos":
                pass
            elif opcion == "Eliminar alimentos":
                with st.form(key="form"):
                    listaNombresAlimentos = []
                    for x in range(0, len(alimentos)):
                        listaNombresAlimentos.append(alimentos[x].getNombre())

                    # OBTENER EL INDEX DEL ELEMENTO A ELIMINAR
                    index = st.selectbox("Seleccione el habitat a eliminar", range(len(listaNombresAlimentos)),
                                         format_func=lambda x: listaNombresAlimentos[x])

                    submit_button = st.form_submit_button(label="EliminarAlim")

                if submit_button:
                    #eliminar
                    # recargar la página para actualizar el selectbox
                    st.experimental_rerun()
                    pass
                else:
                    pass
