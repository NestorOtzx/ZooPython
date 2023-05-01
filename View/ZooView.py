import streamlit as st
from streamlit_option_menu import option_menu

class ZooView:
    def __init__(self, controller):
        self.controller = controller
        self.configuracionDePagina()
        self.__desactivarLinksEnTitulos__()

    def paginaPrincipal(self):
        with st.sidebar:
            opcion = option_menu(menu_title="Panel de control", options=["Inicio", "Ver Animales", "Configurar Animales", "Ver Habitats", "Configurar Habitats", "Ver Alimentos", "Configurar alimentos"],
                                 icons=["border-all", "egg-fill", "gear", "flower3", "gear", "basket-fill", "gear"], menu_icon="display")
        self.controller.seleccionarPagina(opcion)

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