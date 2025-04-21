import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("model.pkl", "rb") as f:
    model, feature_names, label_encoders = pickle.load(f)

st.set_page_config(page_title="🧬 Healthcare Prediction", layout="centered")
st.title("🩺 Personalized Healthcare & Medicine Prediction")
st.write("Enter patient data below to get prediction.")

# Dynamic input fields
user_input = []
for feature in feature_names:
    value = st.number_input(f"{feature}", value=0.0)
    user_input.append(value)

# Predict on submit
if st.button("Predict"):
    input_data = np.array([user_input])
    prediction = model.predict(input_data)[0]
    st.success(f"🧠 Prediction result: **{prediction}**")
