import streamlit as st
from streamlit_option_menu import option_menu

class ZooView:
    def __init__(self, controller):
        self.controller = controller
        self.configuracionDePagina()
        self.__desactivarLinksEnTitulos__()

    # Muestra una barra lateral por la cual el usuario puede navegar por la página web.
    def paginaPrincipal(self):
        with st.sidebar:
            opcion = option_menu(menu_title="Panel de control", options=["Inicio", "Ver Animales", "Configurar Animales", "Ver Habitats", "Configurar Habitats", "Ver Alimentos", "Configurar alimentos"],
                                 icons=["border-all", "egg-fill", "gear", "flower3", "gear", "basket-fill", "gear"], menu_icon="display")
        self.controller.seleccionarPagina(opcion)

    # Por defecto, en cada título o subtitulo se muestra un símbolo de link que en ocasiones puede ser molesto,
    # Esta función es llamada al inicio para desactivar esos símbolos
    def __desactivarLinksEnTitulos__(self):
        st.markdown("""
                                <style>
                                .css-15zrgzn {display: none}
                                .css-eczf16 {display: none}
                                .css-jn99sy {display: none}
                                </style>
                                """, unsafe_allow_html=True)

    # Configuración básica de la página del Zoológico
    def configuracionDePagina(self):
        st.set_page_config(
            page_title="Zoológico",
            layout="wide",
            menu_items={
                'About': "Panel de control de zoológico que permite editar distintos aspectos del mismo, Hecho por Nestor Ortiz, GitHub: https://github.com/NestorOtzx/ZooPython"
            },
            page_icon="https://cdn.pixabay.com/photo/2017/07/20/07/05/giraffe-2521453_960_720.png"
        )