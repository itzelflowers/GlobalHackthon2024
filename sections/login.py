# Importar librerías necesarias.
import streamlit as st
from utils.firebase_utils import login_session
# Conexión a base de datos.
from utils.firebase import Firebase
from sections import register_places, home, see_places, user_home, recomendaciones, sectores, visited_places
from streamlit_lottie import st_lottie
#from streamlit_option_menu import option_menu
import json
from sections.membership import display_rewards_table

# Acceso a Firebase.
db = Firebase().getdb()

def obtener_datos_usuario():
    # Aquí iría el código para conectarte a la base de datos y recuperar los datos
    nombre = db.child(st.session_state['ID']).child('name').get().val()
    apellido = db.child(st.session_state['ID']).child('last_name').get().val()
    correo = db.child(st.session_state['ID']).child('email').get().val()
    datos_usuario = {
        "Nombre": nombre,
        "Correo Electrónico": correo,
        "Apellido": apellido
        
    }
    return datos_usuario

def load_lottiefile(filepath: str):
    with open(filepath, "r") as file:
        return json.load(file)

def app():

    # Inicialización de valores.
    if 'ID' not in st.session_state:
        st.session_state['ID'] = ''
    if 'user_type' not in st.session_state:
        st.session_state['user_type'] = ''
    if 'name' not in st.session_state:
        st.session_state['name'] = ''
    if 'bss_type' not in st.session_state:
        st.session_state['bss_type'] = ''
    if 'last_name' not in st.session_state:
        st.session_state['last_name'] = ''
    if 'signedout' not in st.session_state:
        st.session_state['signedout'] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False


    # Botón de acción para logout.
    def logout_session():
        st.session_state['signedout'] = False
        st.session_state['signout'] = False
        st.session_state['ID'] = ''
        if st.session_state['user_type'] == 'bussines':
            st.session_state['name'] = ''
            st.session_state['bss_type'] = ''
        else:
            st.session_state['name'] = ''
            st.session_state['last_name'] = ''
        st.session_state['user_type'] = ''
    
    
    button_css = """
    <style>
    div.stButton > button:first-child {
        background-color: #f97316;  /* Color naranja para contraste */
        color: #ffffff;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #fb923c;  /* Color más claro para el hover */
        border: none;
    }
    </style>
    """
    
    st.markdown(button_css, unsafe_allow_html=True)

    # Información de login.
    if not st.session_state['signedout']:
        st.sidebar.image('./img/logo_empresa.jpeg', use_column_width=True, width=180)
        st.sidebar.title("Login") 
        st.sidebar.write("Sign in to see more features")
        text_email = st.sidebar.text_input('Email', key='email')
        text_password = st.sidebar.text_input('Password', type='password', key='password')
        # Enviar información.
        st.sidebar.button("Login", on_click=login_session, args=(text_email, text_password))

    # Sesión Iniciada.
    if st.session_state['signout']:
        st.sidebar.image('./img/logo_empresa.jpeg', use_column_width=True, width=180)
        st.sidebar.title("Welcome")
        
        
        if st.session_state['user_type'] == 'bussines':
            st.session_state['name'] = db.child(st.session_state.ID).child('name').get().val()
            st.session_state['bss_type'] = db.child(st.session_state.ID).child('bss_type').get().val()
            st.sidebar.subheader(f'{st.session_state["name"]}')
            st.sidebar.markdown(f'**Business Type**: {st.session_state["bss_type"]}')
            if st.sidebar.button("Register your places"):
                st.session_state.selection = "LUGARES"
            if st.sidebar.button("See your places"):
                st.session_state.selection = "VER_LUGARES"
            
            # Options.
            if "selection" not in st.session_state:
                register_places.app()
            elif st.session_state.selection == "REGISTRAR":
                register_places.app()
            elif st.session_state.selection == "LUGARES":
                register_places.app()
            elif st.session_state.selection == "VER_LUGARES":
                see_places.app()
            else: 
                register_places.app()
        else:
            
            st.session_state['name'] = db.child(st.session_state.ID).child('name').get().val()
            st.session_state['last_name'] = db.child(st.session_state.ID).child('last_name').get().val()
            st.sidebar.subheader(f'{st.session_state["name"]} {st.session_state["last_name"]}')
            if st.sidebar.button("Home"):
                st.session_state.selection = "INICIO"
            if st.sidebar.button("Profile"):
                st.session_state.selection = "PERFIL"
            if st.sidebar.button("Sectors"):
                st.session_state.selection = "SECTORES"
            if st.sidebar.button("Rewards"):
                st.session_state.selection = "RECOMPENSAS"
            if st.sidebar.button("Recommendations"):
                st.session_state.selection = "RECOMENDACIONES"    
            if st.sidebar.button("Visited places"):
                st.session_state.selection = "VISITED"            
                
            # Options.
            if "selection" not in st.session_state:
                user_home.app()
            elif st.session_state.selection == "REGISTRAR":
                user_home.app()
            elif st.session_state.selection == "INICIO":
                user_home.app()
            elif st.session_state.selection == "RECOMENDACIONES":
                recomendaciones.app()
            elif st.session_state.selection == "SECTORES":
                sectores.app()
            elif st.session_state.selection == "PERFIL":
                datos_usuario = obtener_datos_usuario()
                st.title("Traveler's data: 📄")
                st.write(f"**First name:** {datos_usuario['Nombre']} 👤")
                st.write(f"**Last name* {datos_usuario['Apellido']} 👥")
                st.write(f"**Email:** {datos_usuario['Correo Electrónico']} 📧")
                st.write(f"**Type of user:** {st.session_state['user_type']} 🛂")
                st.write(f"**ID:** {st.session_state['ID']} 🔖")
                st.write("Usuario desde: 14 de Abril de 2024 📅")
                # Mostrar esta animación en el cuerpo principal
                lottie_intro = load_lottiefile("./img/place2.json") 
                st_lottie(lottie_intro)
            elif st.session_state.selection == "RECOMPENSAS":
                display_rewards_table()
            elif st.session_state.selection == "VISITED":
                visited_places.app()
            else:
                user_home.app()
        st.sidebar.button("Cerrar Sesión", on_click=logout_session)

        with st.sidebar:
            st_lottie(lottie_intro) 

