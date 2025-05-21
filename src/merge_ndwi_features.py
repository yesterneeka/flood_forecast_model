import pandas as pd
import os

# Loading upstream features (precipitation + temperature)
df_up = pd.read_csv("data/processed/upstream_daily_features.csv")

# Loading downstream discharge data
df_down = pd.read_csv("data/processed/downstream_discharge.csv")

# Converting date columns to datetime
df_up["date"] = pd.to_datetime(df_up["date"])
df_down["valid_time"] = pd.to_datetime(df_down["valid_time"])

# Merging on date
df = pd.merge(df_up, df_down, left_on="date", right_on="valid_time")

df.drop(columns=["valid_time"], inplace=True)

# Normalizing precipitation and discharge for NDWI proxy
df["precip_norm"] = (df["precip_mm"] - df["precip_mm"].min()) / (
    df["precip_mm"].max() - df["precip_mm"].min()
)
df["discharge_norm"] = (df["discharge_m3s"] - df["discharge_m3s"].min()) / (
    df["discharge_m3s"].max() - df["discharge_m3s"].min()
)

# Calculating NDWI proxy
df["ndwi_proxy"] = (df["precip_norm"] - df["discharge_norm"]) / (
    df["precip_norm"] + df["discharge_norm"]
)

# Saving to features directory
os.makedirs("data/features", exist_ok=True)
df.to_csv("data/features/ndwi_features.csv", index=False)

print(" Saved: data/features/ndwi_features.csv")
