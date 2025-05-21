import streamlit as st
import numpy as np
import joblib

# Load the trained model dictionary
model_data = joblib.load("linear_model.pkl")
theta = model_data["theta"]
mean = model_data["mean"]
std = model_data["std"]

st.set_page_config(page_title="Flood Risk Forecast", layout="centered")
st.title("🌊 7-Day Flood Risk Predictor")

st.markdown("Enter NDWI values for the last 3 upstream weeks:")

# Input values
ndwi1 = st.number_input("NDWI Week 1", value=0.0, format="%.4f")
ndwi2 = st.number_input("NDWI Week 2", value=0.0, format="%.4f")
ndwi3 = st.number_input("NDWI Week 3", value=0.0, format="%.4f")

if st.button("Predict Flood Level"):
    X_input = np.array([[ndwi1, ndwi2, ndwi3]])
    X_input_norm = (X_input - mean) / std
    X_input_final = np.hstack([np.ones((1, 1)), X_input_norm])
    prediction = theta.dot(X_input_final.T).item()

    # Interpreting the result
    if prediction < 1.0:
        label = " Low"
    elif prediction < 1.8:
        label = " Medium"
    else:
        label = " High"

    st.markdown(f"### Predicted Flood Level: **{label}**  \nScore: `{prediction:.2f}`")
