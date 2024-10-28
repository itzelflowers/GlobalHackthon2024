import streamlit as st
from utils.firebase import Firebase
    

def app():
    st.title("Register Spaces")
    st.write("Here you can register spaces of your property")
    place = st.text_input('Place name')
    country = st.text_input('Country')
    x = st.text_input("Latitude")
    y = st.text_input("Longitude")
    bss_type = st.selectbox('Space Type', ['Hotel', 'Coworking', 'Coliving', "Cafeteria", "Other"])
    rules = st.text_area("Rules")
    details = st.text_area("Details")


    
    submit = st.button("Create Space")
    # Enviar información.
    if submit:           
        db = Firebase().getdb()
        db.child("Lugares").child(place).child('Place').set(place)
        db.child("Lugares").child(place).child('x').set(x)
        db.child("Lugares").child(place).child('y').set(y)
        db.child("Lugares").child(place).child('bss_type').set(bss_type)
        db.child("Lugares").child(place).child('owner').set(st.session_state.ID)
        db.child("Lugares").child(place).child('country').set(country)
        db.child("Lugares").child(place).child('rules').set(rules)
        db.child("Lugares").child(place).child('details').set(details)
        st.success('The place has been created successfully.')
        st.balloons()