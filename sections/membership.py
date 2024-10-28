import streamlit as st

def display_rewards_table():
    st.markdown("""
        <style>
        .rewards-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 25px;
            text-align: center;
        }
        .rewards-table th, .rewards-table td {
            padding: 15px;
            border-bottom: 1px solid #ddd;
        }
        .rewards-table th {
            background-color: #3fb0e8;
            color: white;
        }
        .rewards-table tr:hover {
            background-color: #f1f1f1;
        }
        .important {
            font-weight: bold;
            font-size: larger;
        }
        .emoji {
            font-size: larger;
        }
        </style>
        
        <h2 style="text-align:center; color: #3fb0e8;"><span class="emoji">🏆</span> ¡Tabla de Recompensas Exclusivas! <span class="emoji">🎁</span></h2>
        <p style="text-align:center;">En <span class="important">Nuestro Club de Recompensas</span>, cada punto cuenta. <span class="emoji">✨</span> Tu fidelidad se traduce en <span class="important">experiencias increíbles</span> y beneficios que sólo mejoran con el tiempo.</p>
        <p style="text-align:center;">Desde <span class="important">descuentos</span> hasta <span class="important">regalos exclusivos</span>, tu viaje con nosotros será <span class="important">siempre gratificante</span>. <span class="emoji">🚀</span></p>
        
        <table class="rewards-table">
            <tr>
                <th>Nivel</th>
                <th>Puntos para acumular</th>
                <th>Beneficios</th>
            </tr>
            <tr>
                <td>Aprendiendo a Viajar</td>
                <td>3,000 puntos</td>
                <td>$100 de descuento en restaurantes</td>
            </tr>
            <tr>
                <td>Viajero Junior</td>
                <td>10,000 puntos</td>
                <td>50% de descuento en restaurantes seleccionados<br>Gift card de mes de cumpleaños</td>
            </tr>
            <tr>
                <td>Trotamundos</td>
                <td>15,000 puntos</td>
                <td>70% de descuento en restaurantes y museos seleccionados<br>Gift card de mes de cumpleaños<br>3 actividades culturales gratis</td>
            </tr>
        </table>
        
        <h3 style="text-align:center; color: #f97316;"><span class="emoji">🌟</span> Sumérgete en el Sistema de Recompensas <span class="emoji">🌟</span></h3>
        <p style="text-align:justify; margin: 0 20px;">Cada <span class="important">interacción</span>, cada <span class="important">compra</span>, y cada <span class="important">recomendación</span> te acerca a niveles más <span class="important">altos de recompensas</span>. Con nuestra escala progresiva, no solo acumulas puntos, sino también <span class="important">experiencias memorables</span>. <span class="emoji">😍</span> Al ser parte de nuestro programa, te aseguras de que cada aventura sea tan <span class="important">enriquecedora</span> como la última. <span class="emoji">❤️</span></p>
        <p style="text-align:justify; margin: 0 20px;">¡No esperes más! Comienza a acumular puntos hoy y descubre los <span class="important">tesoros</span> que hemos preparado para ti. Con cada nivel que alcances, <span class="important">las sorpresas serán aún mayores</span>. ¿Listo para empezar? <span class="emoji">🎉</span></p>
    """, unsafe_allow_html=True)

# Para usar en app.py simplemente llamarías a esta función:
# display_rewards_table()
