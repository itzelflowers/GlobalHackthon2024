import streamlit as st
from utils.firebase import Firebase

alcaldias = ['Azcapotzalco',' Coyoacán', 'Cuajimalpa de Morelos', 'Gustavo A. Madero',
             'Iztacalco','Iztapalapa','La Magadalena Contreras', 
             'Milpa Alta', 'Álvaro Obregón', 'Tláhuac','Tlalpan','Xochimilco',
             'Benito Juárez','Cuauhtémoc','Miguel Hidalgo','Venustiano Carranza']
    

def app():
    st.title("Registra Negocios")
    st.write("Aquí puedes registrar negocios de tu propiedad")
    place = st.text_input('Nombre del lugar')
    location = st.selectbox('Selecciona una alcaldía', alcaldias)
    x = st.text_input("Latitud")
    y = st.text_input("Longitud")
    bss_type = st.selectbox('Tipo de Empresa', ['Comida', 'Cultura', 'Entretenimiento'])
    sillas_ruedas = st.radio("¿Tienes sillas de ruedas?", ("Sí", "No"))
    estacionamiento = st.radio("¿Estacionamiento para personas con capacidades distintas?", ("Sí", "No"))
    rampas = st.radio("¿Cuentas con rampas?", ("Sí", "No"))
    elevadores = st.radio("¿Cuentas con elevadores?", ("Sí", "No"))
    asistencia = st.radio("¿Cuentas con personal de asistencia?", ("Sí", "No"))
    submit = st.button("Crear Negocio")
    # Enviar información.
    if submit:           
        db = Firebase().getdb()
        db.child("Lugares").child(place).child('Place').set(place)
        db.child("Lugares").child(place).child('Location').set(location)
        db.child("Lugares").child(place).child('x').set(x)
        db.child("Lugares").child(place).child('y').set(y)
        db.child("Lugares").child(place).child('bss_type').set(bss_type)
        db.child("Lugares").child(place).child('sillas_ruedas').set(sillas_ruedas)
        db.child("Lugares").child(place).child('estacionamiento').set(estacionamiento)
        db.child("Lugares").child(place).child('rampas').set(rampas)
        db.child("Lugares").child(place).child('elevadores').set(elevadores)
        db.child("Lugares").child(place).child('asistencia').set(asistencia)
        db.child("Lugares").child(place).child('owner').set(st.session_state.ID)
        st.success('El negocio ha sido creada correctamente.')
        st.balloons()