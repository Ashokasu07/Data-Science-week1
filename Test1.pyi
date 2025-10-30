# Task 1: Calculate the overall average temperature.
import pandas as pd

df = pd.read_csv("Data-Science-week1/wetter.csv", parse_dates=["Datum"])
avg_temp = df["Temperatur"].mean()
print(f"The average temperature is {avg_temp:.2f}°C")

# Task 2: Calculate the average temperature for the month of July.
july_avg_temp = df.loc[df["Datum"].dt.month == 7, "Temperatur"].mean()
print(f"The average temperature in July is {july_avg_temp:.2f}°C")

# Compare whether the months of July and May differ significantly in their average temperature.
may_avg_temp = df.loc[df["Datum"].dt.month == 5, "Temperatur"].mean()
print(f"The average temperature in July is {may_avg_temp:.2f}°C")
if abs(july_avg_temp - may_avg_temp) > 5:
    print("July and May differ significantly in their average temperature.")
else:
    print("July and May do not differ significantly in their average temperature.")
