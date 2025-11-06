import pandas as pd

a = [1, 2, 3, 4, 5]
myvar = pd.Series(a, index=["mon", "tue", "wed", "thu", "fri    "])
print(myvar)
print(myvar["tue"])
