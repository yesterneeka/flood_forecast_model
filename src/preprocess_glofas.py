import xarray as xr
import pandas as pd
import os

# Path to downloaded GloFAS file
nc_path = "data/raw/glofas/glofas_downstream_april.nc"

# Loading dataset
ds = xr.open_dataset(nc_path)

print(ds)

# Variable: 'dis24' — discharge in m3/s in last 24h
if "dis24" not in ds:
    raise ValueError("⚠️ Expected variable 'dis24' not found in dataset.")

# Averaging across spatial dimensions (lat, lon)
discharge = ds["dis24"].mean(dim=["latitude", "longitude"])

# Converting to DataFrame
df = discharge.to_dataframe().reset_index()
df.rename(columns={"dis24": "discharge_m3s"}, inplace=True)

# Saving processed CSV
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/downstream_discharge.csv", index=False)

print(" Saved: data/processed/downstream_discharge.csv")
