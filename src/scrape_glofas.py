import cdsapi
import os

# Creating output folder
output_dir = "data/raw/glofas"
os.makedirs(output_dir, exist_ok=True)

# Initializing CDS API client
c = cdsapi.Client()

# Correcting dataset: reforecast (modelled discharge)
c.retrieve(
    "cems-glofas-reforecast",
    {
        "system_version": "version_3_1",
        "variable": "river_discharge_in_the_last_24_hours",
        "product_type": "ensemble_perturbed_forecasts",
        "year": "2024",
        "month": "04",
        "day": [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
        ],
        "leadtime_hour": "24",
        "format": "netcdf",
        "area": [29.5, 70.9, 29.0, 71.5],  # [North, West, South, East]
    },
    f"{output_dir}/glofas_downstream_april.nc",
)

print(" GloFAS downstream discharge downloaded.")
