import streamlit as st
from streamlit_option_menu import option_menu
from Utilidades import Utilidades


class AnimalesView:
    MAX_HORAS_DORMIR = 10
    MAX_EDAD_ANIMAL = 50

    def __init__(self, controller):
        self.controller = controller

    def verAnimales(self, animales, alimentos):
        st.header("Animales del zoológico")
        self.mostrarAnimalesDisponibles(animales, mostrarInteracciones= True, alimentos = alimentos)

    # Muestra una lista dada de animales
    # En caso de proporcionar habitats,
    # se mostrarán los habitats disponibles en el zoológico para asignárselos al animal.
    # En caso de que mostrarInteracciones sea verdadero,
    # se mostrarán las acciones que el animal puede realizar
    # En caso de proporcionar alimentos
    # Al ejecutar la acción "Comer" se mostrarán las opciones de alimento que el animal puede consumir.
    def mostrarAnimalesDisponibles(self, animales, habitats = [], mostrarInteracciones = False, alimentos = []):
        if len(animales) < 1:
            st.subheader("No hay animales en el zoológico")
        else:
            st.divider()
            for i in range(0, len(animales)):
                col1, col2, col3, col4 = st.columns((3, 2, 2, 3))

                fotoDelAnimal = animales[i].getImagen()

                if mostrarInteracciones:
                    st.markdown("## Interactuar con animal")
                    accion = st.selectbox("¿Que debe hacer el animal?", ("Nada", "Comer", "Dormir", "Jugar"),
                                          key="Accion" + str(i))
                    parametro = None

                    if accion == "Comer":
                        if len(alimentos) < 1:
                            st.markdown("#### No hay alimentos disponibles")
                        else:
                            nombresAlimentos = []
                            for x in range(0, len(alimentos)):
                                nombresAlimentos.append(alimentos[x].getNombre())

                            alimentosIndex = st.selectbox("¿Que alimento se le dará al animal?", range(len(nombresAlimentos)),
                                                             format_func=lambda x: nombresAlimentos[x],
                                                             key="alimento" + str(i))

                            st.markdown("#### Cantidad de alimento "+ str(alimentos[alimentosIndex].getCantidad()))

                            parametro = alimentos[alimentosIndex]


                    elif accion == "Dormir":
                        parametro = st.slider("¿Cuantas horas debe dormir?", 1, self.MAX_HORAS_DORMIR)

                    if st.button("Ejecutar acción", key="BotonpyAccion" + str(i)):
                        try:
                            animales[i].ejecutarAccion(accion, parametro)
                            fotoDelAnimal = animales[i].getImagen(accion)
                        except ValueError as e:
                            st.error(e)
                        except Exception as e:
                            st.error(e)

                        # Si no hay error
                        else:
                            st.experimental_rerun()

                with col4:
                    if len(habitats) > 0:
                        st.markdown("### Configurar hábitat")

                        listaTiposHabitat = ["Ninguno"]
                        for j in range(0, len(habitats)):
                            listaTiposHabitat.append(habitats[j].getNombre())

                        nuevoHabitatIndex = st.selectbox("Asignar hábitat", range(len(listaTiposHabitat)),
                                                         format_func=lambda x: listaTiposHabitat[x],
                                                         key="selectHabitat" + str(i))

                        if st.button("Asignar nuevo hábitat", key="AssHab" + str(i)):

                            if not animales[i].getHabitat() is None:
                                animales[i].getHabitat().eliminarAnimal(animales[i])
                                animales[i].setHabitat(None)

                            if nuevoHabitatIndex == 0:
                                # Asignar que no tiene habitat
                                animales[i].setHabitat(None)
                            else:
                                # asignando habitat nuevo
                                try:
                                    animales[i].setHabitat(habitats[nuevoHabitatIndex - 1])
                                    habitats[nuevoHabitatIndex - 1].agregarAnimal(animales[i])
                                except Exception as e:
                                    st.error(e)

                with col1:
                    st.image(fotoDelAnimal)

                with col3:
                    st.markdown("### \
                                &nbsp;")

                    st.markdown("Edad: " + str(animales[i].getEdad()) + " años")
                    st.markdown("Estado de salud: " + str(animales[i].getSalud()))
                    st.markdown("Temperatura habitable: entre " + str(animales[i].getTemperatura()[0]) + " y " + str(
                        animales[i].getTemperatura()[1]) + " °C")

                with col2:
                    st.markdown("### " + animales[i].getNombre())
                    st.markdown("Especie: " + str(animales[i].getEspecie()))
                    st.markdown("Dieta: " + str(animales[i].getDieta()))

                    if animales[i].getHabitat() is None:
                        st.write("Hábitat: Ninguno")
                    else:
                        st.write("Hábitat: " + animales[i].getHabitat().getNombre())

                st.divider()

    # Permite crear y borrar animales en el zoológico, además de crearlos,
    # también se les puede asignar un nuevo habitat una vez agregados al zoológico
    def configurarAnimales(self, animales, habitats):
        col1, col2 = st.columns((1,2), gap="large")

        listaNombresAnimales = []
        for x in range(0, len(animales)):
            listaNombresAnimales.append(animales[x].getNombre())

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
                    especie = st.selectbox("Seleccione el tipo de animal",
                                               ("Jirafa", "Oso polar", "Panda", "Pez payaso", "Pingüino", "Serpiente", "Tiburón", "Tigre"))

                    edad = st.slider("Seleccione la edad del animal", 0, self.MAX_EDAD_ANIMAL)

                    estadoSalud = st.selectbox("Seleccione el estado de salud del animal", ("Sano", "Enfermo"))


                    submit_button = st.form_submit_button(label="Agregar")

                if submit_button:
                    self.controller.agregarAnimal(Utilidades.obtenerNombreRepetido(listaNombresAnimales, nombre), especie, edad, estadoSalud)
                else:
                    pass
            elif opcion == "Eliminar animal":
                with st.form(key="form"):


                    # OBTENER EL INDEX DEL ELEMENTO A ELIMINAR
                    index = st.selectbox("Seleccione el animal a eliminar", range(len(listaNombresAnimales)), format_func=lambda x: listaNombresAnimales[x])

                    submit_button = st.form_submit_button(label="Eliminar")
                if submit_button:
                    self.controller.eliminarAnimal(index)

                    # recargar la página para actualizar el selectbox
                    st.experimental_rerun()
                    pass
                else:
                    pass

        with col2:
            self.mostrarAnimalesDisponibles(animales, habitats)


