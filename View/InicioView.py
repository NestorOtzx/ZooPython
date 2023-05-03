import streamlit as st
import requests



class InicioView:
    def __init__(self, controller):
        self.controller = controller

    def inicio(self):



        col1, col2, col3 = st.columns((1,3,1))

        with col1:
            st.write(' ')

        with col2:
            st.header("Inicio")

            url = "https://swapi.dev/api/people/1/"

            llamado = requests.get(url)

            if llamado.status_code == 200:
                datos = llamado.json()

                for llave, valor in datos.items():
                    st.write(valor)
            else:
                st.error("Error: "+str(llamado.status_code))
                pass

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
