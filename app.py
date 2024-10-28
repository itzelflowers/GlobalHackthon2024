# Importar las librerías necesarias.
import streamlit as st
from sections import login, maps,home
from utils.firebase import Firebase
import json

# Registro de empresas.
def bussines_register():
    st.title("Company registration")
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    name = st.text_input('Company name')
    bss_type = st.selectbox('Business type', ['Hotel', 'Coworking', 'Coliving', "Cafeteria", "Other"])
    submit = st.button("Create company")

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
        st.success('The account has been created successfully.')
        st.balloons()

        # Limpiar información.
        email = ''
        password = ''
        name = ''
        bss_type = ''


# Registro de usuarios.
def user_register():
    st.title("Traveler registration")
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    name = st.text_input('First Name')
    last_name = st.text_input("Last Name")
    submit = st.button("Create user")
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
        st.success('The account has been created successfully')
        st.balloons()

        # Limpiar información.
        email = ''
        password = ''
        name = ''
        last_name = ''


def register():
    st.title("Register here!")
    selected_option = st.radio("What type of user are you?", ("Traveler", "Company"))
    if selected_option == 'Traveler':
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
        if st.button("Register"):
            st.session_state.selection = "REGISTRAR"
