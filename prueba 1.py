import streamlit as st
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:37:49 2024

@author: anicr
"""

import streamlit.components.v1 as components

# Definir el HTML y CSS directamente en una cadena de texto
html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Open+Sans:wght@400;700&display=swap');

@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap'); /* OSWALD */

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap'); /* PLAYFAIR DISPLAY */

@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');

@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap');

body {
    font-family: 'Roboto', sans-serif;
}

.title {
    font-family: 'Playfair Display', serif;
    font-size: 2.5em;
    color: #333;
}

.subtitle {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 2em;
    color: #666;
}

.custom-text {
    font-family: 'Open Sans', sans-serif;
    font-size: 1.2em;
    color: #444;
}
</style>
</head>
<body>
<h1 class="title">Título con Open Sans</h1>
<h2 class="subtitle">Subtítulo con Roboto</h2>
<p class="custom-text">Este es un párrafo con Open Sans.</p>
<p>Este es un párrafo con la tipografía predeterminada (Roboto).</p>
</body>
</html>
"""

# Renderizar el componente HTML en Streamlit
components.html(html_code, height=400)


st.title("Mi Aplicación Streamlit")
st.header("Este es un header")
st.subheader("Este es un subheader")
st.text("Este es un texto simple.")
st.selectbox("Elige una opción", ["Opción 1", "Opción 2", "Opción 3"])