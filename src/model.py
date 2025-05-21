import pandas as pd
import numpy as np
import os

# Loading processed NDWI features
df = pd.read_csv("data/final/flood_data.csv")

print(" Data shape:", df.shape)
print("Columns:", df.columns)
print(df.head())

# Features and target
X = df[["NDWI_Week1", "NDWI_Week2", "NDWI_Week3"]].values
y = df["Flood_Level"].values

print(" X shape:", X.shape)
print(" y shape:", y.shape)

# bias
X_b = np.hstack([np.ones((X.shape[0], 1)), X])  # shape: (n_samples, 4)

# Train-test split (80/20)
split_idx = int(0.8 * len(X_b))
X_train, X_test = X_b[:split_idx], X_b[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

print(" X_train shape:", X_train.shape)
print(" y_train shape:", y_train.shape)

# pseudo-inverse to avoid singular matrix errors
if X_train.size > 0 and y_train.size > 0:
    theta = np.linalg.pinv(X_train) @ y_train
    y_pred = X_test @ theta
    mse = np.mean((y_pred - y_test) ** 2)
    print(f" Model trained (manual OLS). MSE: {mse:.2f}")

    # Saving predictions
    df_out = pd.DataFrame({"Actual": y_test.flatten(), "Predicted": y_pred.flatten()})
    os.makedirs("data/results", exist_ok=True)
    df_out.to_csv("data/results/predictions.csv", index=False)
    print(" Saved predictions: data/results/predictions.csv")
else:
    print(" Training data is empty. Cannot train model.")
