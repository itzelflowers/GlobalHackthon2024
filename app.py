# Importar las librerías necesarias.
import streamlit as st
from sections import login, maps,home
from utils.firebase import Firebase
import json
import plotly.graph_objects as go

# Registro de empresas.
def bussines_register():
    st.title("Registro de Empresas")
    email = st.text_input('Correo Electrónico')
    password = st.text_input('Contraseña', type='password')
    name = st.text_input('Nombre Empresa')
    bss_type = st.selectbox('Tipo de Empresa', ['Comida', 'Cultura', 'Entretenimiento'])
    submit = st.button("Crear Empresa")

    # Enviar información.
    if submit:           
        db = Firebase().getdb()
        auth = Firebase().getauth()
        user = auth.create_user_with_email_and_password(email, password)
        db.child(user['localId']).child('ID').set(user['localId'])
        db.child(user['localId']).child('email').set(email)
        db.child(user['localId']).child('password').set(password)
        db.child(user['localId']).child('user_type').set('bussines')
        db.child(user['localId']).child('name').set(name)
        db.child(user['localId']).child('bss_type').set(bss_type)
        st.success('La cuenta ha sido creada correctamente.')
        st.balloons()

        # Limpiar información.
        email = ''
        password = ''
        name = ''
        bss_type = ''


# Registro de usuarios.
def user_register():
    st.title("Registro de Usuarios")
    email = st.text_input('Correo Electrónico')
    password = st.text_input('Contraseña', type='password')
    name = st.text_input('Nombre')
    last_name = st.text_input("Apellidos")
    submit = st.button("Crear Usuario")
    # Enviar información.
    if submit:           
        db = Firebase().getdb()
        auth = Firebase().getauth()
        user = auth.create_user_with_email_and_password(email, password)
        db.child(user['localId']).child('ID').set(user['localId'])
        db.child(user['localId']).child('email').set(email)
        db.child(user['localId']).child('password').set(password)
        db.child(user['localId']).child('user_type').set('client')
        db.child(user['localId']).child('name').set(name)
        db.child(user['localId']).child('last_name').set(last_name)
        st.success('La cuenta ha sido creada correctamente.')
        st.balloons()

        # Limpiar información.
        email = ''
        password = ''
        name = ''
        last_name = ''


def register():
    st.title("Registrate")
    selected_option = st.radio("¿Qué tipo de usuario eres?", ("Cliente", "Empresa"))
    if selected_option == 'Cliente':
        user_register()
    else:
        bussines_register()


# Configuración de Streamlit.
st.set_page_config(
    page_title="Access Places | Home",
    page_icon="🗺️",
    initial_sidebar_state="expanded",
)

# Iniciar Sesión.
login.app()


# Si hay usuario.
if st.session_state['user_type'] != '':
    pass
# No hay usuario.
else:
    if "selection" not in st.session_state:
        home.app()
        st.subheader("Do you want to explore more places?")
        if st.button("Register"):
            st.session_state.selection = "REGISTER"
    elif st.session_state.selection == "REGISTER":
        register()
    else:
        home.app()
        #####
        # Cargar los polígonos desde el archivo JSON
        json_path = "./img/image_polygons.json"
        with open(json_path, "r") as f:
            polygons = json.load(f)

        # Crear una figura de Plotly
        fig = go.Figure()

        # Dibujar cada polígono
        for polygon in polygons:
            x = [point[0] for point in polygon]  # Extraer coordenadas X
            y = [point[1] for point in polygon]  # Extraer coordenadas Y

            # Cerrar el polígono uniendo el último punto con el primero
            x.append(polygon[0][0])
            y.append(polygon[0][1])

            # Añadir el polígono a la figura
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', fill='toself', name='Polígono'))

        # Configurar el diseño de la figura
        fig.update_layout(
            title="Polígonos del Plano",
            xaxis=dict(title='Coordenada X'),
            yaxis=dict(title='Coordenada Y', scaleanchor="x", scaleratio=1),
            showlegend=False,
            height=800,
        )

        # Mostrar la figura en Streamlit
        st.title("Visualización de Polígonos del Plano")
        st.plotly_chart(fig, use_container_width=True)
    
        #####
        st.subheader("¿Quieres explorar más lugares?")
        
        if st.button("Registrar"):
            st.session_state.selection = "REGISTRAR"
