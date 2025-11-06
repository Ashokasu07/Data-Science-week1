import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data-Science-week1/wetter.csv")
print(pd.options.display.max_columns)
print(pd.options.display.max_rows)
print(df.head())
df.info()
# df.plot()
# plt.show()
