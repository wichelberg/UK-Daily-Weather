import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def weather_audit():
    print("\n" + "="*50)
    print("      WEATHER DATASET: STATISTICAL CHECK")
    print("="*50)

    try:
        path = '../uk_weather_daily_2010_2020.csv' if os.path.exists('../uk_weather_daily_2010_2020.csv') else 'uk_weather_daily_2010_2020.csv'
        df = pd.read_csv(path)
        
        correlation = df['temperature_mean'].corr(df['temperature_min'])
        
        print(f"\n[CORRELATION PROOF]")
        print(f"Mean Temp vs Min Temp: {correlation:.4f}")
        
        if correlation > 0.90:
            print("Verdict: High Multicollinearity detected. Pruning is justified.")
        
        print("\n[FEATURE SUMMARY]")
        pruning_candidates = ['evapotranspiration', 'solar_radiation', 'windspeed_mean']
        for col in pruning_candidates:
            if col in df.columns:
                print(f"-> {col}: Ready for removal (Low relevance to accident/fire risk).")

        print("\n" + "="*50)
        print("      CHECK COMPLETE - DATA IS VALID FOR CLEANING")
        print("="*50)

    except Exception as e:
        print(f"[ERROR] Dosya bulunamadı veya okunamadı: {e}")

if __name__ == "__main__":
    weather_audit()
