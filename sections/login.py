# Importar librerías necesarias.
import streamlit as st
from utils.firebase_utils import login_session
# Conexión a base de datos.
from utils.firebase import Firebase
from sections import register_places, home, see_places, user_home, recomendaciones, sectores, visited_places, add_space
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
        background-color: #10b981;  /* Green color for contrast */
        color: #ffffff;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #34d399;  /* Lighter green for hover */
        border: none;
    }
    </style>
"""

    st.markdown(button_css, unsafe_allow_html=True)

    # Información de login.
    if not st.session_state['signedout']:
        st.sidebar.image('./img/logoAP.png', use_column_width=True, width=180)
        st.sidebar.title("Login") 
        st.sidebar.write("Log in to see more features")
        text_email = st.sidebar.text_input('Email', key='email')
        text_password = st.sidebar.text_input('Password', type='password', key='password')
        # Enviar información.
        st.sidebar.button("Login", on_click=login_session, args=(text_email, text_password)) 

    # Sesión Iniciada.
    if st.session_state['signout']:
        # st_lottie(lottie_intro)
        st.sidebar.image('./img/logoAP.png', use_column_width=True, width=180)
        st.sidebar.title("Welcome")
        
        
        if st.session_state['user_type'] == 'bussines':
            st.session_state['name'] = db.child(st.session_state.ID).child('name').get().val()
            st.session_state['bss_type'] = db.child(st.session_state.ID).child('bss_type').get().val()
            st.sidebar.subheader(f'{st.session_state["name"]}')
            st.sidebar.markdown(f'**Industry of the Company**: {st.session_state["bss_type"]}')
            if st.sidebar.button("Register Places"):
                st.session_state.selection = "LUGARES"
            if st.sidebar.button("Add Spaces"):
                st.session_state.selection = "AGREGAR_LUGAR"
            if st.sidebar.button("View Spaces"):
                st.session_state.selection = "VER_LUGARES"
            
            # Options.
            if "selection" not in st.session_state:
                register_places.app()
            elif st.session_state.selection == "LUGARES":
                register_places.app()
            elif st.session_state.selection == "VER_LUGARES":
                see_places.app()
            elif st.session_state.selection == "AGREGAR_LUGAR":
                add_space.app()
            else: 
                register_places.app()
        else:
            
            st.session_state['name'] = db.child(st.session_state.ID).child('name').get().val()
            st.session_state['last_name'] = db.child(st.session_state.ID).child('last_name').get().val()
            st.sidebar.subheader(f'{st.session_state["name"]} {st.session_state["last_name"]}')
            if st.sidebar.button("Inicio"):
                st.session_state.selection = "Home"
            if st.sidebar.button("Perfil"):
                st.session_state.selection = "Profile"
            if st.sidebar.button("Sectores"):
                st.session_state.selection = "Sectors"
            if st.sidebar.button("Recompensas"):
                st.session_state.selection = "Rewars"
            if st.sidebar.button("Recomendaciones"):
                st.session_state.selection = "Recommendations"    
            if st.sidebar.button("Visited Places"):
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
                st.title("User Information 📄")
                st.write(f"**Name:** {datos_usuario['Name']} 👤")
                st.write(f"**Lastname:** {datos_usuario['Lastname']} 👥")
                st.write(f"**Email Address:** {datos_usuario['Email']} 📧")
                st.write(f"**User Type:** {st.session_state['user_type']} 🛂")
                st.write(f"**ID:** {st.session_state['ID']} 🔖")
                st.write("User since: October 29, 2024 📅")
            elif st.session_state.selection == "RECOMPENSAS":
                display_rewards_table()
            elif st.session_state.selection == "VISITED":
                visited_places.app()
            else:
                user_home.app()
        st.sidebar.button("Log Out", on_click=logout_session)
