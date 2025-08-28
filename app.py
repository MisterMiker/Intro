import streamlit as st
from PIL import Image

st.title("Mi primera App!!")

image = Image.open('Lol.jpg')
st.image(image, caption='Papu')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)
