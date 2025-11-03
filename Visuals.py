import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\deeku\Desktop\Dummy Data\wetter.csv")
df.head()
df.info()
df.tail(5)
df.describe()
df.plot(
    kind="line",
    title="Wetter",
    x="Datum",
    xlabel="Dates",
    y="Temperatur",
    ylabel="Temperature",
    color="blue",
)
df1 = pd.read_excel(
    r"C:\Users\deeku\Desktop\Dummy Data\world_population_excel_workbook.xlsx"
)
df1
df1.plot(
    kind="bar",
    title="World Population",
    x="Continent",
    xlabel="Continents",
    y="2020 Population",
    ylabel="Population 2020",
    color="green",
)
df2 = pd.read_csv(
    r"C:\Users\deeku\Desktop\Dummy Data\Germany Foreign Population\12521-0001_en.csv",
    sep=";",
    skiprows=7,
    skipfooter=4,
    engine="python",
)
df2
cols_named_unwanted = [
    c for c in df2.columns if any(s in c.lower() for s in ("unnamed:2", "unnamed:4"))
]
# drop columns whose values (after stripping) are all "e"
cols_all_e = [c for c in df2.columns if df2[c].astype(str).str.strip().eq("e").all()]

# drop entirely empty columns
cols_all_na = [c for c in df2.columns if df2[c].isna().all()]

cols_to_drop = list(dict.fromkeys(cols_named_unwanted + cols_all_e + cols_all_na))
if cols_to_drop:
    df2 = df2.drop(columns=cols_to_drop)

print("Dropped columns:", cols_to_drop)
print("Remaining columns:", list(df2.columns))
df2.rename(columns={"Unnamed: 0": "Date"}, inplace=True)
df2.head()
print(list(df2.columns))
df2.plot(
    kind="line",
    title="Germany Foreign Population",
    x="Date",
    xlabel="Years",
    y="Total",
    ylabel="Population",
    color="red",
)
df2["Female"].plot(
    kind="bar", stacked=True, title="Germany Foreign Population"
)  # Stacked bar chart for only Female population
df2["Total"].plot.barh(stacked=True)  # Stacked horizontal bar chart for all population
df2.plot.scatter(
    x="Male", y="Female", title="Male vs Female Population", s=50, color="purple"
)  # Scatter plot for Male vs Female population
df2.plot.hist(
    bin=10, title="Population Distribution", figsize=(10, 6)
)  # Histogram for population distribution
df2.plot.box(title="Population Box Plot")  # Box plot for population
df2.plot.area(
    title="Population Area Plot",
    alpha=0.4,
)  # Area plot for population
df2.plot.pie(
    y="Total", title="Total Population Pie Chart"
)  # Pie chart for total population
