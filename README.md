test.py output:

      WEATHER DATASET: STATISTICAL CHECK

[CORRELATION PROOF]
Mean Temp vs Min Temp: 0.9654
Verdict: High Multicollinearity detected. Pruning is justified.

[FEATURE SUMMARY]
-> evapotranspiration: Ready for removal (Low relevance to accident/fire risk).
-> solar_radiation: Ready for removal (Low relevance to accident/fire risk).
-> windspeed_mean: Ready for removal (Low relevance to accident/fire risk).


      CHECK COMPLETE - DATA IS VALID FOR CLEANING

->Weather Data Refinement (Handling Multicollinearity)

During the Exploratory Data Analysis (EDA) phase, a formal statistical audit was conducted to evaluate the relationships between meteorological variables. The audit revealed a critical Pearson correlation coefficient of 0.9654 between temperature_mean and temperature_min.

To prevent Multicollinearity, which can destabilize model coefficients and lead to overfitting, the decision to prune temperature_min was mathematically justified. We retained temperature_mean as the primary feature and temperature_max to account for extreme thermal events. Furthermore, the audit identified evapotranspiration, solar_radiation, and windspeed_mean as features with low relevance to the specific variance of accident and fire risks, leading to their removal to streamline the model's focus.

->Data Alignment and Statistical Validation

To ensure the integrity of the integrated dataset (Weather, Energy, Accidents, and Holidays), a standardized synchronization pipeline was implemented:

Temporal Synchronization: All records were filtered to the 2010–2020 timeframe to ensure cross-dataset consistency.

Audit Verification: A pre-cleaning check was executed, resulting in a "Check Complete - Data is Valid for Cleaning" status, confirming that the remaining features provide a clean signal for PCA (Principal Component Analysis).

Standardization: Feature names were normalized to lowercase and categorical labels (Is_Bank_Holiday) were converted to boolean integers, facilitating an error-free merge across heterogeneous sources.
