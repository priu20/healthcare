import streamlit as st  # type: ignore
import numpy as np  # type: ignore
import pickle
import xgboost  # type: ignore  # Required so pickle can resolve the XGBoost classes

# Load the trained model
with open("model.pkl", "rb") as f:
    model, feature_names, label_encoders = pickle.load(f)

# Streamlit page config
st.set_page_config(page_title="🧬 Healthcare Prediction", layout="centered")
st.title("🩺 Personalized Healthcare & Medicine Prediction")
st.write("Enter patient data below to get a prediction:")

# Dynamic input fields
user_input = []
for feature in feature_names:
    value = st.number_input(f"{feature}", value=0.0, format="%.4f")
    user_input.append(value)

# Predict on submit
if st.button("Predict"):
    input_array = np.array([user_input])
    try:
        prediction = model.predict(input_array)[0]
        st.success(f"🧠 Prediction result: **{prediction}**")
    except Exception as e:
        st.error(f"❌ Prediction failed: {str(e)}")
