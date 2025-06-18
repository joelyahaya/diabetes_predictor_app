
import streamlit as st
import numpy as np
from joblib import load

# Load the trained model
model = load('diabetes_prediction_model.joblib')

st.set_page_config(page_title="Diabetes Predictor", layout="centered")
st.title("🩺 Diabetes Risk Prediction App")
st.write("Input patient health data below to assess diabetes risk.")

def get_user_input():
    pregnancies = st.number_input("Pregnancies", min_value=0)
    glucose = st.number_input("Glucose", min_value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0)
    insulin = st.number_input("Insulin", min_value=0)
    bmi = st.number_input("BMI", min_value=0.0, step=0.1)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, step=0.01)
    age = st.number_input("Age", min_value=0)

    data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    return data

user_data = get_user_input()

if st.button("Predict"):
    prediction = model.predict(user_data)
    result = "🔴 Diabetic" if prediction[0] == 1 else "🟢 Not Diabetic"
    st.subheader("Prediction Result")
    st.success(result)


st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-size: 14px; color: gray;'>"
    "Designed and developed by:<br>"
    "<b>Yahaya Joel Casmed</b><br>"
    "<b>Samuel Agyarko Boakye</b><br>"
    "<b>Coffie Jones</b>"
    "</div>",
    unsafe_allow_html=True
)
