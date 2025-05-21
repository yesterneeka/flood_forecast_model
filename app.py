import streamlit as st
import numpy as np
import joblib

# Load the trained model
model_data = joblib.load("linear_model.pkl")
theta = model_data["theta"]  # shape: (4,)
mean = model_data["mean"]  # shape: (3,)
std = model_data["std"]  # shape: (3,)

# Streamlit page settings
st.set_page_config(page_title="Flood Risk Forecast", layout="centered")
st.title("🌊 7-Day Flood Risk Predictor")
st.markdown(
    "Enter NDWI values for the **last 3 upstream weeks** to estimate downstream flood risk."
)

# Input fields
ndwi1 = st.number_input("NDWI Week 1", value=0.0, format="%.4f")
ndwi2 = st.number_input("NDWI Week 2", value=0.0, format="%.4f")
ndwi3 = st.number_input("NDWI Week 3", value=0.0, format="%.4f")

# Prediction button
if st.button("Predict Flood Level"):
    # Step 1: Form input array
    X_input = np.array([[ndwi1, ndwi2, ndwi3]])

    # Step 2: Normalize using training mean and std
    X_input_norm = (X_input - mean) / std

    # Step 3: Add intercept term
    X_input_final = np.hstack([np.ones((1, 1)), X_input_norm])  # shape: (1, 4)

    # Step 4: Predict using theta (manual OLS)
    prediction = float(X_input_final @ theta)

    # Step 5: Map to label
    if prediction < 1.0:
        label = "🟢 Low"
    elif prediction < 1.8:
        label = "🟡 Medium"
    else:
        label = "🔴 High"

    # Display result
    st.markdown(f"### Predicted Flood Level: **{label}**  \nScore: `{prediction:.2f}`")
