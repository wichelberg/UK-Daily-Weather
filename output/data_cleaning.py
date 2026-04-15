import pandas as pd
weather_df = pd.read_csv('uk_weather_daily_2010_2020.csv')

weather_cleaned = weather_df.drop([
    'temperature_min', 
    'evapotranspiration', 
    'solar_radiation', 
    'windspeed_mean'
], axis=1)
weather_cleaned['date'] = pd.to_datetime(weather_cleaned['date'])
weather_cleaned.to_csv('weather_data_daily_2010to2020.csv', index=False)