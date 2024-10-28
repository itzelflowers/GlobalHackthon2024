# Import the libraries needed.
import streamlit as st
from sections import maps

# Initial app.
def app():
    st.title("Welcome to Access Places", anchor=None)
    
    # Styles.
    st.markdown("""
        <style>
            .slogan {
                padding-left: 1em;
            }
            .map-container {
                padding: 2em 0em;
            }
            .qual-list {
                padding-right: 1em;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Slogan and description.
    st.write('<div class="slogan"><h2>Places that suits you all over the world 🌍</h2></div>', unsafe_allow_html=True)
    st.markdown("""
    **Access Places** is the guide to find places that suits to your necesities. We are committed to ensuring that you have the best experience in the places you visit, 
                imagine arriving at a place, knowing that you will always find it available,
                without worrying about it being busy.
    """)
    
    # List of cualities.
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown('<div class="qual-list"><h3>What do we offer?</h3>', unsafe_allow_html=True)
        st.markdown("""
        - Guaranteed accessibility 🚪
        - Active comunity 👥
        - Benefits and discounts 🎁
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="map-container">', unsafe_allow_html=True)
        maps.app()
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("""
    Join Hidden Places and be part of the adventure. Your next great experience starts here!
    """)

    st.write('<br>', unsafe_allow_html=True)