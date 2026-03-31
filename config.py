# config.py
LOCATIONS = {
    "England": [
        {"name": "London", "lat": 51.51, "lon": -0.13},
        {"name": "Birmingham", "lat": 52.48, "lon": -1.89},
        {"name": "Manchester", "lat": 53.48, "lon": -2.24},
        {"name": "Leeds", "lat": 53.80, "lon": -1.55},
        {"name": "Bristol", "lat": 51.45, "lon": -2.59},
    ],
    "Wales": [
        {"name": "Cardiff", "lat": 51.48, "lon": -3.18},
        {"name": "Swansea", "lat": 51.62, "lon": -3.94},
        {"name": "Aberystwyth", "lat": 52.41, "lon": -4.08},
    ],
    "Scotland": [
        {"name": "Edinburgh", "lat": 55.95, "lon": -3.19},
        {"name": "Glasgow", "lat": 55.86, "lon": -4.25},
        {"name": "Aberdeen", "lat": 57.15, "lon": -2.11},
        {"name": "Inverness", "lat": 57.48, "lon": -4.22},
    ],
}

DAILY_VARS = [
    "temperature_2m_mean", "temperature_2m_max", "temperature_2m_min",
    "precipitation_sum", "windspeed_10m_mean", "windspeed_10m_max",
    "et0_fao_evapotranspiration", "shortwave_radiation_sum",
]

START_DATE = "2010-01-01"
END_DATE = "2020-12-31"
OUTPUT_FILE = "output/uk_weather_daily_2010_2020.csv"