import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales_df = pd.read_csv(
    r"C:\Users\deeku\Desktop\Dummy Data\Open Campus\umsatzdaten_gekuerzt.csv"
)
weather_df = pd.read_csv(r"C:\Users\deeku\Desktop\Dummy Data\Open Campus\wetter.csv")
kiwo_df = pd.read_csv(r"C:\Users\deeku\Desktop\Dummy Data\Open Campus\kiwo.csv")
sales_df.info()
weather_df.info()
kiwo_df.info()
sales_df.head()

# Ensuring date format is consistent
sales_df["Datum"] = pd.to_datetime(sales_df["Datum"], format="%Y-%m-%d")
# Extracting day names from dates
sales_df["Woche"] = sales_df["Datum"].dt.day_name()
# Calculating average sales per day of the week
Average_sales_per_day = (
    sales_df.groupby("Woche")["Umsatz"]
    .mean()
    .reindex(
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    )
)
Average_sales_per_day

# Adding color gradient based on average sales values
norm = (Average_sales_per_day - Average_sales_per_day.min()) / (
    Average_sales_per_day.max() - Average_sales_per_day.min()
)
colors = [(0, norm_val, 0) for norm_val in norm]

# Plotting average sales per day
plt.title("Average Sales per Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Average Sales")
plt.bar(Average_sales_per_day.index, Average_sales_per_day.values, color=colors)
plt.show()
Average_sales_per_day.plot(
    kind="bar",
    title="Average Sales per Day of the Week",
    xlabel="Day of the Week",
    ylabel="Average Sales",
    figsize=(10, 6),
    color="red",
)
