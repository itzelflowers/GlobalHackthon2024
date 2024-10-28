# Importar las librerías necesarias.
# Conexión a base de datos.
from utils.firebase import Firebase
# Variables de proyecto.
import streamlit as st

# Botón de acción para Login.
def login_session(email, password):
    try:
        # Acceso a Firebase.
        db = Firebase().getdb()
        auth = Firebase().getauth()
        # Autenticación.
        user = auth.sign_in_with_email_and_password(email, password)
        st.session_state['signedout'] = True
        st.session_state['signout'] = True
        # Obtener información del usuario.
        st.session_state['ID'] = db.child(user['localId']).child('ID').get().val()
        st.session_state['user_type'] = db.child(user['localId']).child('user_type').get().val()
        st.success("Successful Login")
    except Exception as e:
        st.warning('Login Failed')