import xarray as xr
import pandas as pd
import os

# Loading the .nc file (temperature + precipitation)
era5_path = os.path.join("data", "raw", "era5_april_2mtemp_precip.nc")
ds = xr.open_dataset(era5_path)

ds = ds.rename({"valid_time": "time"})

# Extracting variables
precip = ds["tp"]  # total precipitation (m)
temp = ds["t2m"]  # 2m temperature (K)

# Converting precipitation to mm
precip_mm = precip * 1000

# daily average across grid
daily_precip = precip_mm.mean(dim=["latitude", "longitude"]).resample(time="1D").mean()
daily_temp = temp.mean(dim=["latitude", "longitude"]).resample(time="1D").mean()

# Creating DataFrame
df = pd.DataFrame(
    {
        "date": daily_precip["time"].values,
        "precip_mm": daily_precip.values,
        "temperature_K": daily_temp.values,
    }
)

# Converting temperature from Kelvin to Celsius
df["temperature_C"] = df["temperature_K"] - 273.15
df.drop(columns="temperature_K", inplace=True)

# Saving to CSV
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/upstream_daily_features.csv", index=False)

print(" Saved: data/processed/upstream_daily_features.csv")
