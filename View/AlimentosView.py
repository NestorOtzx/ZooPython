import random
import streamlit as st
from streamlit_option_menu import option_menu
from Utilidades import Utilidades
from streamlit_image_select import image_select

class AlimentosView:
    MAX_CANTIDAD_ALIMENTOS = 10

    def __init__(self, controller):
        self.controller = controller

    # Muestra una lista dada de alimentos junto con sus características y un icono de referencia.
    def mostrarAlimentos(self, alimentos):
        if len(alimentos) < 1:
            st.subheader("No hay alimentos disponibles.")
        else:
            st.divider()
            for x in range(0, len(alimentos)):
                col1, col2 = st.columns((1, 3))

                with col1:
                    st.image(alimentos[x].getImagen())
                with col2:
                    st.markdown("### " + alimentos[x].getNombre())
                    st.markdown("Tipo: " + alimentos[x].getTipo())
                    st.markdown("Cantidad: " + str(alimentos[x].getCantidad()))

                st.divider()

    # Permite crear, editar y borrar alimentos.
    def configurarAlimentos(self, alimentos):

        col1, col2 = st.columns(2, gap="large")
        listaNombresAlimentos = []
        for x in range(0, len(alimentos)):
            listaNombresAlimentos.append(alimentos[x].getNombre())

        with col1:
            st.header("Configuración de alimentos")

            opcion = option_menu(menu_title="Configurar",
                                 options=["Agregar alimentos", "Editar alimentos", "Eliminar alimentos"],
                                 menu_icon="gear")

            if opcion == "Agregar alimentos":

                # Tipo
                st.markdown("### Seleccione el tipo de alimento")
                tipoDieta = st.selectbox("Tipo de alimento", options=("Carnívoro", "Herbívoro"))

                with st.form(key="form"):
                    # Nombre
                    nombre = st.text_input("Nombre del alimento", "Alimento")

                    # Cantidad
                    cantidad = st.slider("Seleccione la cantidad de alimento a agregar", 0, self.MAX_CANTIDAD_ALIMENTOS, value = 1)

                    submit_button = st.form_submit_button(label="Agregar")

                if submit_button:
                    if (tipoDieta == "Carnívoro"):
                        imgs = ["https://cdn.pixabay.com/photo/2014/12/21/23/57/meat-576422_960_720.png",
                                "https://cdn.pixabay.com/photo/2012/04/13/01/51/hamburger-31775_960_720.png",
                                "https://cdn.pixabay.com/photo/2014/12/21/23/24/spare-ribs-575310_960_720.png",
                                "https://cdn.pixabay.com/photo/2013/07/12/14/47/meat-148789_960_720.png",
                                "https://cdn.pixabay.com/photo/2017/02/01/00/02/drumstick-2028375_960_720.png"]
                    else:
                        imgs = ["https://cdn.pixabay.com/photo/2013/07/12/19/18/watermelon-154510_960_720.png",
                                "https://cdn.pixabay.com/photo/2012/04/24/16/15/broccoli-40295_960_720.png",
                                "https://cdn.pixabay.com/photo/2013/07/13/12/10/cabbage-159333_960_720.png",
                                "https://cdn.pixabay.com/photo/2013/07/13/13/49/cucumber-161610_960_720.png"]


                    self.controller.agregarAlimento(Utilidades.obtenerNombreRepetido(listaNombresAlimentos, nombre), tipoDieta, cantidad, imgs[random.randint(0, len(imgs)-1)])
                else:
                    pass
            elif opcion == "Editar alimentos":
                if len(alimentos)>0:
                    nombresAlimentos = []
                    for x in range(0, len(alimentos)):
                        nombresAlimentos.append(alimentos[x].getNombre())

                    alimentosIndex = st.selectbox("¿Que alimento quiere editar?", range(len(nombresAlimentos)),
                                                  format_func=lambda x: nombresAlimentos[x],
                                                  key="editarAlimento")

                    with st.form(key = "editarAlimento"):
                        nuevoNombre = st.text_input("Ingrese el nuevo nombre", alimentos[alimentosIndex].getNombre())
                        nuevoTipoDieta = st.selectbox("Nuevo tipo de alimento", options=("Carnívoro", "Herbívoro"),
                                                      index = 0 if alimentos[alimentosIndex].getTipo() == "Carnívoro" else 1)
                        nuevaCantidad = st.slider("Nueva cantidad de alimento", 0, self.MAX_CANTIDAD_ALIMENTOS, value=alimentos[alimentosIndex].getCantidad())
                        nuevaFoto = image_select("Nueva imagen",
                                    ["https://cdn.pixabay.com/photo/2014/12/21/23/57/meat-576422_960_720.png",
                                    "https://cdn.pixabay.com/photo/2012/04/13/01/51/hamburger-31775_960_720.png",
                                    "https://cdn.pixabay.com/photo/2014/12/21/23/24/spare-ribs-575310_960_720.png",
                                    "https://cdn.pixabay.com/photo/2013/07/12/14/47/meat-148789_960_720.png",
                                    "https://cdn.pixabay.com/photo/2017/02/01/00/02/drumstick-2028375_960_720.png",
                                    "https://cdn.pixabay.com/photo/2013/07/12/19/18/watermelon-154510_960_720.png",
                                    "https://cdn.pixabay.com/photo/2012/04/24/16/15/broccoli-40295_960_720.png",
                                    "https://cdn.pixabay.com/photo/2013/07/13/12/10/cabbage-159333_960_720.png",
                                    "https://cdn.pixabay.com/photo/2013/07/13/13/49/cucumber-161610_960_720.png"
                                     ])
                        submit_button = st.form_submit_button(label="Editar")
                    if submit_button:
                        alimentos[alimentosIndex].editarAlimento(nuevoNombre, nuevoTipoDieta, nuevaCantidad, nuevaFoto)

            elif opcion == "Eliminar alimentos":
                if len(alimentos)>0:
                    with st.form(key="form"):


                        # OBTENER EL INDEX DEL ELEMENTO A ELIMINAR
                        index = st.selectbox("Seleccione el alimento a eliminar", range(len(listaNombresAlimentos)),
                                             format_func=lambda x: listaNombresAlimentos[x])

                        submit_button = st.form_submit_button(label="EliminarAlim")

                    if submit_button:
                        self.controller.eliminarAlimento(index)
                        # recargar la página para actualizar el selectbox
                        st.experimental_rerun()
                        pass
        with col2:
            self.mostrarAlimentos(alimentos)


