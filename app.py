import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Loading the trained model
model = joblib.load("linear_model.pkl")

st.set_page_config(page_title="Flood Risk Forecast", layout="centered")

st.title(" 7-Day Flood Risk Predictor")

st.markdown("Enter NDWI values for the last 3 upstream weeks:")

#  NDWI values
ndwi1 = st.number_input("NDWI Week 1", value=0.0, format="%.4f")
ndwi2 = st.number_input("NDWI Week 2", value=0.0, format="%.4f")
ndwi3 = st.number_input("NDWI Week 3", value=0.0, format="%.4f")

if st.button("Predict Flood Level"):
    X_input = np.array([[1, ndwi1, ndwi2, ndwi3]])
    prediction = model.dot(X_input.T).item()

    # Interpreting the result
    predicted_class = round(prediction)
    label = {0: "🟢 Low", 1: "🟡 Medium", 2: "🔴 High"}.get(predicted_class, " Unknown")

    st.markdown(f"### Predicted Flood Level: **{label}** (score: {prediction:.2f})")
