# 🌊 Flood Forecast: NDWI-Based Early Warning System

This project predicts downstream flood risk based on upstream environmental indicators like precipitation, temperature, and runoff using a simplified NDWI proxy and a manually implemented linear regression model.

## WebApp Link
https://floodforecastmodel.streamlit.app

## Project Structure

- `data/raw/`: Raw ERA5 and GloFAS `.nc` files
- `data/processed/`: Preprocessed CSVs (e.g., upstream precipitation, downstream discharge)
- `data/features/`: Engineered NDWI-based features
- `data/final/`: Merged dataset with flood labels for model training
- `data/results/`: Model predictions and evaluation
- `src/`: All Python scripts (scraping, preprocessing, modeling, etc.)

## Data Sources

- [ERA5 Reanalysis](https://cds.climate.copernicus.eu/) – temperature, precipitation, runoff
- [GloFAS](https://www.globalfloods.eu/) – river discharge (downstream)

## Workflow

1. **Data Collection**: ERA5 and GloFAS data for April 1–21, 2024
2. **Preprocessing**: Convert `.nc` files to CSV, normalize features
3. **Feature Engineering**: Compute NDWI proxy:  
   \[
   \text{NDWI_proxy} = \frac{\text{Precipitation} - \text{Discharge}}{\text{Precipitation} + \text{Discharge}}
   \]
4. **Labeling**: Assign flood levels (`0=low`, `1=medium`, `2=high`)
5. **Modeling**: Manual implementation of linear regression (OLS)
6. **Evaluation**: Mean Squared Error on predicted flood levels

## Result

- Final model trained on 6 valid data points
- MSE ≈ 2.30 (based on test set)

## Future Work

- Visualizations (NDWI timeline, predicted vs actual floods)
- Web interface: 7-day flood risk forecast from NDWI input

## Author

Aneeka Khan – LUMS Final Year Project
