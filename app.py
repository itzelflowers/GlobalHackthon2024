# Importar las librerías necesarias.
import streamlit as st
from sections import login, maps,home
from utils.firebase import Firebase

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
    page_title="Hidden Places | Home",
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
        st.subheader("¿Quieres explorar más lugares?")
        if st.button("Registrar"):
            st.session_state.selection = "REGISTRAR"
    elif st.session_state.selection == "REGISTRAR":
        register()
    else:
        home.app()
        st.subheader("¿Quieres explorar más lugares?")
        if st.button("Registrar"):
            st.session_state.selection = "REGISTRAR"
