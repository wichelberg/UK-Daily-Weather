# main.py
import pandas as pd
import os
import time
from config import LOCATIONS, DAILY_VARS, START_DATE, END_DATE, OUTPUT_FILE
from api_client import get_weather_client, fetch_point_data

def run_pipeline():
    client = get_weather_client()
    country_dfs = []

    for i, (country, points) in enumerate(LOCATIONS.items()):
        print(f"\n{country} processing...")
        
        if i > 0:
            print("API safety wait: Sleeping for 70 seconds to reset rate limit...")
            time.sleep(70)

        point_dfs = []
        for point in points:
            print(f"  Fetching: {point['name']}")
            df_point = fetch_point_data(client, point['lat'], point['lon'], START_DATE, END_DATE, DAILY_VARS)
            point_dfs.append(df_point)
            time.sleep(0.5) 

        df_country = pd.concat(point_dfs).groupby("date").mean().reset_index()
        df_country.insert(0, "country", country)
        country_dfs.append(df_country)

    final = pd.concat(country_dfs, ignore_index=True)
    final['date'] = pd.to_datetime(final['date'])
    final = final[final['date'].between('2010-01-01', '2020-12-31')]
    final['date'] = final['date'].dt.date

    num_cols = final.select_dtypes(include="number").columns
    final[num_cols] = final[num_cols].round(3)

    if not os.path.exists('output'): os.makedirs('output')
    final.to_csv(OUTPUT_FILE, index=False)
    print(f"\ndone, saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    run_pipeline()