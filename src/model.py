import pandas as pd
import numpy as np
import os
import joblib

print(" Running UPDATED model.py")

# Loading data
df = pd.read_csv("data/final/flood_data.csv")
print(" Data shape:", df.shape)
print("Columns:", df.columns)
print(df.head())

# Extracting features and target
X = df[["NDWI_Week1", "NDWI_Week2", "NDWI_Week3"]].values
y = df["Flood_Level"].values

print(" X shape:", X.shape)
print(" y shape:", y.shape)

# Normalize features
mean = X.mean(axis=0)
std = X.std(axis=0)
X = (X - mean) / std

# bias term
X_b = np.hstack([np.ones((X.shape[0], 1)), X])

# Train/test split
split_idx = int(0.8 * len(X_b))
X_train, X_test = X_b[:split_idx], X_b[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

print(" X_train shape:", X_train.shape)
print(" y_train shape:", y_train.shape)

# Training model (OLS)
if X_train.size > 0 and y_train.size > 0:
    theta = np.linalg.pinv(X_train) @ y_train
    y_pred = X_test @ theta

    # Clamping predictions
    y_pred = np.clip(y_pred, 0, 2)

    mse = np.mean((y_pred - y_test) ** 2)
    print(f" Model trained (manual OLS). MSE: {mse:.2f}")

    # Saving predictions
    os.makedirs("data/results", exist_ok=True)
    pd.DataFrame({"Actual": y_test.flatten(), "Predicted": y_pred.flatten()}).to_csv(
        "data/results/predictions.csv", index=False
    )
    print(" Saved predictions: data/results/predictions.csv")

    # saving the model and normalizer
    model_data = {"theta": theta, "mean": mean, "std": std}
    model_path = os.path.join(os.getcwd(), "linear_model.pkl")
    joblib.dump(model_data, model_path)
    print(f" Model saved to: {model_path}")

else:
    print(" Training data is empty. Cannot train model.")
