# Importar librerías necesarias.
# Web.
import streamlit as st
from streamlit_folium import st_folium
# Data.
import geopandas
from shapely.geometry import LineString
import folium
from utils.firebase import Firebase

db = Firebase().getdb()

def app():
    st.title("Add Spaces to your Places")
    lugares = db.child('Lugares').get().val()
    places=list()
    for l in lugares:
        lugar = db.child('Lugares').child(l).child('owner').get().val()
        if lugar == st.session_state.user:
            places.append(lugar)
    places = list(set(places))
    selected_option = st.radio("What type of user are you?", ("Event", "Space"))
    if selected_option == 'Event':
        event_register(places)
    else:
        space_register(places)


def space_register(places):
    st.title("Add a Space")
    st.write("Select the place where you want to add a space")
    selected_place = st.selectbox("Places", places)
    st.write("Select the type of space you want to add")
    selected_type = st.text_input("Example: Kitchen")
    st.write("Ocupability")
    occp = st.text_input("10")
    st.write("Status")
    status = st.text_input("Busy")
    submit = st.button("Create Space")
    # Enviar información.
    if submit:          
        db.child("Lugares").child(selected_place).child('Place').set(selected_type)
        db.child("Lugares").child(selected_place).child('x').set(occp)
        db.child("Lugares").child(selected_place).child('y').set(status)
        st.success('The place has been created successfully.')
        st.balloons()
def event_register(places):
    pass
