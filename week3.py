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
