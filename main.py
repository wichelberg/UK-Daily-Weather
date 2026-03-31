# main.py
import pandas as pd
import os
import time
from config import LOCATIONS, DAILY_VARS, START_DATE, END_DATE, OUTPUT_FILE
from api_client import get_weather_client, fetch_point_data

def run_pipeline():
    client = get_weather_client()
    country_dfs = []

    # Use enumerate to get the index (i)
    for i, (country, points) in enumerate(LOCATIONS.items()):
        print(f"\n{country} işleniyor...")
        
        # Only sleep if it's NOT the first country (i > 0)
        if i > 0:
            print("API safety wait: Sleeping for 60 seconds to reset rate limit...")
            time.sleep(60)

        point_dfs = []
        for point in points:
            print(f"  Fetching: {point['name']}")
            df_point = fetch_point_data(client, point['lat'], point['lon'], START_DATE, END_DATE, DAILY_VARS)
            point_dfs.append(df_point)
            # Short sleep between cities to be safe
            time.sleep(1.5) 

        # Country-based averaging
        df_country = pd.concat(point_dfs).groupby("date").mean().reset_index()
        df_country.insert(0, "country", country)
        country_dfs.append(df_country)

    # Birleştirme ve Kaydetme
    final = pd.concat(country_dfs, ignore_index=True)
    num_cols = final.select_dtypes(include="number").columns
    final[num_cols] = final[num_cols].round(3)

    if not os.path.exists('output'): os.makedirs('output')
    final.to_csv(OUTPUT_FILE, index=False)
    print(f"\nİşlem tamam! Veri şuraya kaydedildi: {OUTPUT_FILE}")

if __name__ == "__main__":
    run_pipeline()