import pandas as pd
import matplotlib.pyplot as plt
import os

# Loading processed flood data
df = pd.read_csv("data/final/flood_data.csv", parse_dates=["date"])

# Plot for NDWI over time
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["NDWI_Week1"], label="NDWI Week 1", marker="o")
plt.plot(df["date"], df["NDWI_Week2"], label="NDWI Week 2", marker="o")
plt.plot(df["date"], df["NDWI_Week3"], label="NDWI Week 3", marker="o")
plt.title("NDWI Values Over Time")
plt.xlabel("Date")
plt.ylabel("NDWI")
plt.grid(True)
plt.legend()
os.makedirs("data/plots", exist_ok=True)
plt.savefig("data/plots/ndwi_over_time.png")
plt.close()

# Loading predictions
pred_df = pd.read_csv("data/results/predictions.csv")

# Plot for predictions vs actual
plt.figure(figsize=(8, 5))
plt.plot(pred_df["Actual"], label="Actual", marker="o")
plt.plot(pred_df["Predicted"], label="Predicted", marker="x", linestyle="--")
plt.title("Actual vs Predicted Flood Levels")
plt.xlabel("Sample")
plt.ylabel("Flood Level")
plt.grid(True)
plt.legend()
plt.savefig("data/plots/flood_level_comparison.png")
plt.close()

print(" Saved visualizations in data/plots/")
