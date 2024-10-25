'''import streamlit as st
from datetime import datetime

hoy = datetime.now()
dia = hoy.day

@st.dialog("Recordatorio")
def recordatorio_descargas():
        st.write(f"¡Se recomienda descargar la base de datos!")
        #reason = st.text_input("Because...")

        if st.button("Descargar"):
            st.session_state.recordatorio_descargas = 'hola'
            st.rerun()

if dia == 24:
    if "recordatorio_descargas" not in st.session_state:
        recordatorio_descargas()

    else:
        st.write('Descargado!')'''

# Doble dialogo
import streamlit as st
import time

@st.dialog("Aviso de Descarga")
def aviso_descarga():
    st.write("¡Se recomienda descargar la base de datos!")

    if st.button("Descargar"):
        st.session_state["aviso_descarga"] = True
        st.rerun()


@st.dialog("Confirmación de Acción")
def confirmacion_accion():
    st.write("Esta acción ha sido confirmada.")

    if st.button("Aceptar"):
        st.session_state["confirmacion_accion"] = True
        st.rerun()


# Botón para activar el primer diálogo
if "aviso_descarga" not in st.session_state:
    st.button("Mostrar Aviso de Descarga", on_click=aviso_descarga)
    #import streamlit as st
    #import time

else:
    st.write("Base de datos descargada.")
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.05)  # Simula un proceso
        progress_bar.progress(i + 1)
    st.snow()

# Botón para activar el segundo diálogo
if "confirmacion_accion" not in st.session_state:
    st.button("Mostrar Confirmación de Acción", on_click=confirmacion_accion)
else:
    st.write("Acción confirmada.")
    st.balloons()


import streamlit as st
if st.button('Pedro?'):
    st.balloons()
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2l3ZGMzMzFzcWRxZzUyaTVyMmxuOW5yNWhwM2praTgyZGRmcjh4aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tHIRLHtNwxpjIFqPdV/giphy.webp", width=300)
    # Asegúrate de que el archivo "audio.mp3" está en el mismo directorio
    #audio_file = "C://thesis_PUCP//la canción de pedro __ PEDRO - Raffaella Carrà, Jaxomy, Agatino Romero (Remix) [sub. español]_RXKabdUBiWM.mp3"
    audio_file = "https://github.com/Nestor20193767/Pruebas_stream/blob/main/la%20canci%C3%B3n%20de%20pedro%20__%20PEDRO%20-%20Raffaella%20Carr%C3%A0%2C%20Jaxomy%2C%20Agatino%20Romero%20(Remix)%20%5Bsub.%20espa%C3%B1ol%5D_RXKabdUBiWM.mp3"

    # Reproduce el archivo MP3 en Streamlit
    st.audio(audio_file, format="audio/mp3", autoplay=True, start_time="26s")
