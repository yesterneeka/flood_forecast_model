import pandas as pd
import os

# Loading NDWI features
df = pd.read_csv("data/features/ndwi_features.csv")
df["date"] = pd.to_datetime(df["date"])


# Helper to encode flood levels
def encode_flood_level(discharge):
    if discharge < 82:
        return 0  # Low
    elif discharge < 84:
        return 1  # Medium
    else:
        return 2  # High


df["Flood_Level"] = df["discharge_m3s"].apply(encode_flood_level)

# Generating lagged NDWI columns
records = []
for i in range(14, len(df)):
    row = {
        "date": df.loc[i, "date"],
        "NDWI_Week1": df.loc[i - 7, "ndwi_proxy"],
        "NDWI_Week2": df.loc[i - 10, "ndwi_proxy"],
        "NDWI_Week3": df.loc[i - 13, "ndwi_proxy"],
        "Flood_Level": df.loc[i, "Flood_Level"],
    }
    records.append(row)

flood_df = pd.DataFrame(records)

# Saving final dataset
os.makedirs("data/final", exist_ok=True)
flood_df.to_csv("data/final/flood_data.csv", index=False)
print("Saved: data/final/flood_data.csv")
