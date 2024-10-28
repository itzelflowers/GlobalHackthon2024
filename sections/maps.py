# Import libraries needed.
import streamlit as st
from streamlit_folium import st_folium
# Data.
import geopandas
from shapely.geometry import LineString
import folium
from utils.firebase import Firebase
db = Firebase().getdb()


# Map Initialization.
def init_map(center=(1.2868736122709594, 103.85484853562664), zoom_start=10, map_type="cartodbpositron"):
    return folium.Map(location=center, zoom_start=zoom_start, tiles=map_type, width='50%', height='50%')

def app():
    m = init_map()
    # Get places.
    lugares = db.child('Lugares').get().val()
    for l in lugares:
        lugar = db.child('Lugares').child(l).child('Country').get().val()
        if lugar == 'Singapur':
            x = db.child('Lugares').child(l).child('x').get().val()
            y = db.child('Lugares').child(l).child('y').get().val()
            folium.Marker([float(x), float(y)], tooltip=f'{l}').add_to(m)
    level1_map_data = st_folium(m)
    st.session_state.selected_id = level1_map_data['last_object_clicked_tooltip']
    if st.session_state.selected_id is not None:
        st.subheader(f'{st.session_state.selected_id}')
        st.write(f'Business Type: {db.child("Lugares").child(st.session_state.selected_id).child("bss_type").get().val()}')