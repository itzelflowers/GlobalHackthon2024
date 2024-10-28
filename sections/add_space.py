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
    st.title("Your Businesses")
    places = []
    lugares = db.child('Lugares').get().val()
    for l in lugares:
        lugar = db.child('Lugares').child(l).child('owner').get().val()
        if st.session_state.ID == lugar:
            places.append(l)
    places = list(set(places))
    selected_option = st.radio("What type of user are you?", ("Event", "Space"))
    if selected_option == 'Event':
        event_register(places)
    else:
        space_register(places)


def space_register(places):
    st.title("Add a Space")
    selected_place = st.selectbox("Select the place where you want to add a space", places)
    st.write("Select the type of space you want to add")
    selected_type = st.text_input("Select the type of space you want to add")
    occp = st.text_input("Ocupability")
    status = st.text_input("Status")
    submit = st.button("Create Space")
    # Enviar información.
    if submit:          
        db.child("Lugares").child(selected_place).child('spaces').child(selected_type).set(selected_type)
        db.child("Lugares").child(selected_place).child('spaces').child(selected_type).child('occp').set(occp)
        db.child("Lugares").child(selected_place).child('spaces').child(selected_type).child('status').set(status)
        st.success('The place has been created successfully.')
        st.balloons()
def event_register(places):
    st.title("Add a Event")
    selected_place = st.selectbox("Select the place where you want to add a space", places)
    spaces = places.child('spaces')
    selected_spaces = st.selectbox("Select the place where you want to add a space", spaces)
    name_event = st.text_input("Write the name of the event")
    occp = st.text_input("Ocupability")
    status = st.text_input("Status")
    submit = st.button("Create Space")
    # Enviar información.
    if submit:          
        db.child("Lugares").child(selected_place).child('events').child(name_event).set(name_event)
        db.child("Lugares").child(selected_place).child('events').child(name_event).child('selected_spaces').set(selected_spaces)
        db.child("Lugares").child(selected_place).child('events').child(name_event).child('occp').set(occp)
        st.success('The place has been created successfully.')
        st.balloons()
