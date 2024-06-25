import streamlit as st


# Definir el CSS como una cadena de texto
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Open+Sans:wght@400;700&display=swap');

body {
    font-family: 'Roboto', sans-serif;
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
"""

st.header("Este es un header")