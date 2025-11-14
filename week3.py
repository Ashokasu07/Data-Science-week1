import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sales_df = pd.read_csv(
    r"C:\Users\deeku\Desktop\Dummy Data\Open Campus\umsatzdaten_gekuerzt.csv"
)
weather_df = pd.read_csv(r"C:\Users\deeku\Desktop\Dummy Data\Open Campus\wetter.csv")
kiwo_df = pd.read_csv(r"C:\Users\deeku\Desktop\Dummy Data\Open Campus\kiwo.csv")
sales_df.info()
weather_df.info()
kiwo_df.info()
df = sales_df.merge(weather_df, on="Datum", how="left").merge(
    kiwo_df, on="Datum", how="left"
)
df.info()

# Identify numerical columns
num_cols = df.select_dtypes(include=["int64", "float64"]).columns
num_cols

# Plot distributions of numerical columns
for col in num_cols:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f"Distribution of {col}")
    plt.show()

# Scatter plots to explore relationships
sns.scatterplot(data=df, x="Temperatur", y="Umsatz", size=50)
plt.title("Sales Volume vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Sales Volume")
plt.show()

# Scatter plot for KielerWoche
sns.scatterplot(data=df, x="KielerWoche", y="Umsatz", size=50)
plt.title("Sales Volume vs KielerWoche")
plt.xlabel("Temperature (°C)")
plt.ylabel("Sales Volume")
plt.show()

df.columns["kielerWoche"].info()
