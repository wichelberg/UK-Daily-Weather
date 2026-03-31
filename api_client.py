# api_client.py
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

def get_weather_client():
    cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    return openmeteo_requests.Client(session=retry_session)

def fetch_point_data(client, lat, lon, start, end, variables):
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start,
        "end_date": end,
        "daily": variables,
        "timezone": "Europe/London",
    }
    responses = client.weather_api("https://archive-api.open-meteo.com/v1/archive", params=params)
    response = responses[0]
    daily = response.Daily()
    
    # DataFrame oluşturma mantığı
    return pd.DataFrame({
        "date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        ).date,
        "temperature_mean": daily.Variables(0).ValuesAsNumpy(),
        "temperature_max": daily.Variables(1).ValuesAsNumpy(),
        "temperature_min": daily.Variables(2).ValuesAsNumpy(),
        "precipitation": daily.Variables(3).ValuesAsNumpy(),
        "windspeed_mean": daily.Variables(4).ValuesAsNumpy(),
        "windspeed_max": daily.Variables(5).ValuesAsNumpy(),
        "evapotranspiration": daily.Variables(6).ValuesAsNumpy(),
        "solar_radiation": daily.Variables(7).ValuesAsNumpy(),
    })