import streamlit as st
import streamlit.components.v1 as components

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Open+Sans:wght@400;700&display=swap');

body {
    font-family: 'Roboto', sans-serif;
    margin: 0;
    padding: 0;
}

.container {
    padding: 20px;
}

.title {
    font-family: 'Open Sans', sans-serif;
    font-size: 2.5em;
    color: #333;
}

.subtitle {
    font-family: 'Roboto', sans-serif;
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
<div class="container">
    <h1 class="title">Título con Open Sans</h1>
    <h2 class="subtitle">Subtítulo con Roboto</h2>
    <p class="custom-text">Este es un párrafo con Open Sans.</p>
    <p>Este es un párrafo con la tipografía predeterminada (Roboto).</p>
</div>
</body>
</html>
"""

# Renderizar el componente HTML en Streamlit
components.html(html_code, height=600)

st.header("a ver qué sale")