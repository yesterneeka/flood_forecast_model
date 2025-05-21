import joblib

# Loading the trained model weights
theta = joblib.load("linear_model.pkl")

# Printing the learned coefficients
print("Model weights (theta):", theta)

# Interpretation tip
print("\nInterpretation:")
print("Intercept (bias):", theta[0])
print("Weight NDWI Week 1:", theta[1])
print("Weight NDWI Week 2:", theta[2])
print("Weight NDWI Week 3:", theta[3])
