import streamlit as st
from PIL import Image

st.set_page_config(page_title="Adaptability level to online education", layout='wide')
#A streamlit app with two centered texts with different seizes

st.markdown("<h1 style='text-align: center; color: black;'>Adaptability level to online education</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: black;'>Classification of the student's ability to adapt to online education based on their context </h2>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: black;'>Developed by Nicolás Trianon </h3>", unsafe_allow_html=True)

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local("C://Users//Usuario//Desktop//The Bridge//ML - Trabajo final//src//images//back.jpg")  

img = Image.open("C://Users//Usuario//Desktop//The Bridge//ML - Trabajo final//src//images//efectos-del-coronavirus-sobre-la-educacion.jpg")
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(img)

with col3:
    st.write(' ')

