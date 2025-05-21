import cdsapi

c = cdsapi.Client()

c.retrieve(
    "reanalysis-era5-land",
    {
        "variable": [
            "2m_temperature",
            "total_precipitation",
            "surface_runoff",
            "sub_surface_runoff",
        ],
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
        "time": ["00:00"],
        "area": [37, 72, 34, 76],  # [North, West, South, East]
        "format": "netcdf",
    },
    "data/raw/era5_upstream_april.nc",
)

print(" ERA5 upstream data (temp, precip, runoff) downloaded.")
