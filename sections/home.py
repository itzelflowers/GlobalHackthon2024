import streamlit as st
from sections import maps

def app():
    st.title("Bienvenidos a Hidden Places", anchor=None)
    
    # Estilos para la sangría y el espaciado
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
    
    # Slogan y descripción
    st.write('<div class="slogan"><h2>Explora sin Límites 🌍</h2></div>', unsafe_allow_html=True)
    st.markdown("""
    **Hidden Places** es tu guía para un turismo accesible en la CDMX. Nos comprometemos a que personas con discapacidad motriz y adultos mayores disfruten de cada rincón con total libertad. 

    Con **facilidades accesibles**, comunidad interactiva y beneficios exclusivos, cada visita se convierte en una experiencia inolvidable.

    Las empresas tienen una nueva ventana al mundo del turismo inclusivo, descubriendo oportunidades para todos.
    """)
    
    # Lista de cualidades y el mapa
    col1, col2 = st.columns([1, 2])  # Proporción de columnas: 1 para la lista, 2 para el mapa
    
    with col1:
        st.markdown('<div class="qual-list"><h3>Cualidades de Hidden Places:</h3>', unsafe_allow_html=True)
        st.markdown("""
        - Accesibilidad garantizada 🚪
        - Comunidad activa 👥
        - Beneficios y descuentos 🎁
        - Compromiso con la inclusión 💖
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="map-container">', unsafe_allow_html=True)
        maps.app()
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Texto debajo del mapa
    st.write("""
    Descubre los destinos turísticos más acogedores para todos, con la seguridad y el confort que mereces.

    Únete a Hidden Places y sé parte de la aventura. ¡Tu próxima gran experiencia comienza aquí!
    """)

    # Separación antes del botón
    st.write('<br>', unsafe_allow_html=True)
    
    # Botón para más información o acción
    if st.button('Descubre más sobre Hidden Places'):
        # Acción cuando el botón es presionado
        pass

