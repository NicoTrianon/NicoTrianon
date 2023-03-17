import streamlit as st
import pandas as pd
import pickle as pkl
from PIL import Image
import joblib

st.set_page_config(page_title="Level of adaptability to online education", layout='wide')

st.markdown("<h2 style='text-align: center; color: black;'>Assessment of the level of adaptability of students to online education </h2>", unsafe_allow_html=True)

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

gender = st.selectbox("Student´s gender (0 if girl, 1 if boy):",
                      [0,1])

institution_type = st.selectbox(
    "Institution type (0 if Government, 1 if Non Government):",
    [0,1])

it_student = st.selectbox(
    "IT student (0 if No, 1 if Yes):",
    [0,1])

location = st.selectbox(
    "Location (if the student can attend the class from his house or has to move; 0 if No, 1 if Yes):",
    [0,1])

load_shedding = st.selectbox(
    "Load-shedding (0 if Low, 1 if High):",
    [0,1])

internet_type = st.selectbox(
    "Internet Type (0 if Mobile Data, 1 if Wifi):",
    [0,1])

self_lms = st.selectbox(
    "Self Learning Management System (systematic set of instructions that facilitate learners' mastery of a body of knowledge or a complex process and are designed where the learner is free to choose what to learn, how to learn, when to learn and where to learn; 0 if No, 1 if Yes):",
    [0,1])

age_1 = st.selectbox(
    "Age between 1 & 5 (0 if No, 1 if Yes):",
    [0,1])

age_2 = st.selectbox(
    "Age between 6 & 10 (0 if No, 1 if Yes):",
    [0,1])

age_3 = st.selectbox(
    "Age between 11 & 15 (0 if No, 1 if Yes):",
    [0,1])

age_4 = st.selectbox(
    "Age between 16 & 20 (0 if No, 1 if Yes):",
    [0,1])

age_5 = st.selectbox(
    "Age between 21 & 25 (0 if No, 1 if Yes):",
    [0,1])

age_6 = st.selectbox(
    "Age between 26 & 30 (0 if No, 1 if Yes):",
    [0,1])

max_education_level_1 = st.selectbox(
    "Maximun education level reached: School (0 if No, 1 if Yes):",
    [0,1])

max_education_level_2 = st.selectbox(
    "Maximun education level reached: College (0 if No, 1 if Yes):",
    [0,1])

max_education_level_3 = st.selectbox(
    "Maximun education level reached: University (0 if No, 1 if Yes):",
    [0,1])

financial_condition_1 = st.selectbox(
    "Financial condition: Poor (0 if No, 1 if Yes):",
    [0,1])

financial_condition_2 = st.selectbox(
    "Financial condition: Mid (0 if No, 1 if Yes):",
    [0,1])

financial_condition_3 = st.selectbox(
    "Financial condition: Rich (0 if No, 1 if Yes):",
    [0,1])

net_type_1 = st.selectbox(
    "Network type: 2G (0 if No, 1 if Yes):",
    [0,1])

net_type_2 = st.selectbox(
    "Network type: 3G (0 if No, 1 if Yes):",
    [0,1])

net_type_3 = st.selectbox(
    "Network type: 4G (0 if No, 1 if Yes):",
    [0,1])

class_duration_1 = st.selectbox(
    "Class duration: 0 hours (0 if No, 1 if Yes):",
    [0,1])

class_duration_2 = st.selectbox(
    "Class duration: Between 1 & 3 hours (0 if No, 1 if Yes):",
    [0,1])

class_duration_3 = st.selectbox(
    "Class duration: Between 3 & 6 hours (0 if No, 1 if Yes):",
    [0,1])

device_1 = st.selectbox(
    "Device: Computer (0 if No, 1 if Yes):",
    [0,1])

device_2 = st.selectbox(
    "Device: Mobile (0 if No, 1 if Yes):",
    [0,1])

device_3 = st.selectbox(
    "Device: Tab (0 if No, 1 if Yes):",
    [0,1])

# Creo un array con las opciones elegidas

variables = ['Gender','Institution Type','IT Student','Location','Load-shedding','Internet Type','Self Lms','1-5','11-15','16-20','21-25','26-30','6-10','College','School','University','Mid','Poor','Rich','2G','3G','4G','0','1-3','3-6','Computer','Mobile','Tab']

selections = [['Gender', gender], ['Institution Type', institution_type], ['IT Student', it_student], ['Location', location], ['Load-shedding', load_shedding], ['Internet Type', internet_type], ['Self Lms', self_lms], ['1-5', age_1], ['11-15', age_3], ['16-20', age_4], ['21-25', age_5], ['26-30', age_6], ['6-10', age_2], ['College', max_education_level_2], ['School', max_education_level_1],  ['University', max_education_level_3], ['Mid', financial_condition_2], ['Poor', financial_condition_1], ['Rich', financial_condition_3], ['2G', net_type_1], ['3G', net_type_2], ['4G', net_type_3], ['0', class_duration_1], ['1-3', class_duration_2], ['3-6', class_duration_3], ['Computer', device_1], ['Mobile', device_2], ['Tab', device_3]]

df_selections = pd.DataFrame(selections)

df_selections = df_selections.T

df_selections.columns = df_selections.iloc[0]

df_selections.drop(0, axis=0, inplace=True)

# Cargo mis modelos entrenados

model_multiclass = joblib.load(open(f"C://Users//Usuario//Desktop//The Bridge//ML - Trabajo final//src//model//my_model_multiclass.pkl", "rb"))
model_binary = joblib.load(open(f"C://Users//Usuario//Desktop//The Bridge//ML - Trabajo final//src//model//my_model_binary.pkl", "rb"))

# Realizo la predicción

prediction_1 = model_multiclass.predict(df_selections)  

if st.button("Predict"):
    if prediction_1[0] == 2:
        st.markdown("<h2 style='text-align: center; color: black;'>The level of adaptability of the student to online education is MODERATE </h2>", unsafe_allow_html=True)
        img_mod = Image.open("C://Users//Usuario//Desktop//The Bridge//ML - Trabajo final//src//images//image_moderate.jpg")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(' ')

        with col2:
            st.image(img_mod)

        with col3:
            st.write(' ')

    else:
        prediction_2 = model_binary.predict(df_selections)
        if prediction_2[0] == 1:
            st.markdown("<h2 style='text-align: center; color: black;'>The level of adaptability of the student to online education is LOW </h2>", unsafe_allow_html=True)
            img_low = Image.open("C://Users//Usuario//Desktop//The Bridge//ML - Trabajo final//src//images//image_low.jpg")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.write(' ')

            with col2:
                st.image(img_low)

            with col3:
                st.write(' ')

        elif prediction_2[0] == 3:
            st.markdown("<h2 style='text-align: center; color: black;'>The level of adaptability of the student to online education is HIGH </h2>", unsafe_allow_html=True)
            img_high = Image.open("C://Users//Usuario//Desktop//The Bridge//ML - Trabajo final//src//images//image_high.png")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.write(' ')

            with col2:
                st.image(img_high)

            with col3:
                st.write(' ')

