# Importar librerías necesarias.
# Web.
import streamlit as st
from streamlit_folium import st_folium
# Data.
import geopandas
from shapely.geometry import LineString
import folium
from utils.firebase import Firebase
import random

db = Firebase().getdb()

def app():
    st.title("Your Recommendations")
    st.write("Based on your needs and the amenities these places offer, we recommend the following options.")
    lugares = db.child('Lugares').get().val()
    lugares = list(lugares)
    random.shuffle(lugares)
    lugares = lugares[:10]
    for l in lugares:
        st.subheader(l)