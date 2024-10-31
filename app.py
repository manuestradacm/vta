import streamlit as st

# Listas para almacenar las respuestas
si_van = []
no_van = []

# Título de la aplicación
st.title("Encuesta: ¿Vas a Vallarta?")

# Pedir el nombre del usuario
nombre = st.text_input("Ingresa tu nombre:")

# Pregunta de sí o no
if nombre:
    # Mostrar el botón para registrar la respuesta
    if st.button("Registrar Respuesta"):
        respuesta = st.radio("¿Vas a Vallarta?", ("Sí", "No"))

        # Guardar respuesta en la lista correspondiente
        if respuesta == "Sí":
            si_van.append(nombre)
        else:
            no_van.append(nombre)

        # Mostrar las listas actualizadas
        st.write("### Lista de quienes van a Vallarta")
        st.write(si_van if si_van else "Nadie ha dicho que va a Vallarta.")

        st.write("### Lista de quienes no van a Vallarta")
        st.write(no_van if no_van else "Nadie ha dicho que no va a Vallarta.")
