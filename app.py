import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl","rb"))

st.title("Student Performance Predictor")

gender = st.selectbox("Gender",["Male","Female"])
lunch = st.selectbox("Lunch Type",["Standard","Free/Reduced"])
test = st.selectbox("Test Preparation",["Completed","None"])

reading = st.number_input("Reading Score")
writing = st.number_input("Writing Score")

gender = 1 if gender=="Male" else 0
lunch = 1 if lunch=="Standard" else 0
test = 1 if test=="Completed" else 0

features = np.array([[gender,lunch,test,reading,writing]])

if st.button("Predict"):
    prediction = model.predict(features)
    st.success("Predicted Math Score: {}".format(prediction[0]))