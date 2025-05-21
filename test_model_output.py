import numpy as np
import joblib

# Load model components
model_data = joblib.load("linear_model.pkl")
theta = model_data["theta"]
mean = model_data["mean"]
std = model_data["std"]

# Test 1: Low flood NDWI
ndwi_low = np.array([[-1.0, -0.8, -0.3]])
ndwi_low_norm = (ndwi_low - mean) / std
ndwi_low_input = np.hstack([np.ones((1, 1)), ndwi_low_norm])
pred_low = theta.dot(ndwi_low_input.T).item()
print("Low NDWI prediction:", round(pred_low, 2))

# Test 2: High flood NDWI
ndwi_high = np.array([[0.7, -1.0, -0.9]])
ndwi_high_norm = (ndwi_high - mean) / std
ndwi_high_input = np.hstack([np.ones((1, 1)), ndwi_high_norm])
pred_high = theta.dot(ndwi_high_input.T).item()
print("High NDWI prediction:", round(pred_high, 2))

# Test 3: Medium NDWI
ndwi_med = np.array([[-0.8, -0.9, -0.5]])
ndwi_med_norm = (ndwi_med - mean) / std
ndwi_med_input = np.hstack([np.ones((1, 1)), ndwi_med_norm])
pred_med = theta.dot(ndwi_med_input.T).item()
print("Medium NDWI prediction:", round(pred_med, 2))
