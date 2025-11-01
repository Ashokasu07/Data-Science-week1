import pandas as pd

# 1. Reading a CSV file without header so adding header=None and providing column names using names parameter
df = pd.read_csv(
    r"C:\Users\deeku\Desktop\countries of the world.csv",
    header=None,
    names=["Country", "Region"],
)
print(df)
print(df.head(7))  # Displaying first 7 rows
print(df.tail(3))  # Displaying last 3 rows
print(df.shape)  # Displaying shape of the DataFrame (rows,cols)

# Reading a text file using table or if using read_csv then need to provide separator as sep='\t'
df1 = pd.read_table(r"C:\Users\deeku\Desktop\Dummy Data\countries of the world.txt")
print(df1)
df1.info()  # Displaying info about the DataFrame

df2 = pd.read_json(r"C:\Users\deeku\Desktop\Dummy Data\json_sample.json")
print(df2)

# Excel File Reading but it has multiple sheets so choosing one using sheet_name
df3 = pd.read_excel(
    r"C:\Users\deeku\Desktop\Dummy Data\world_population_excel_workbook.xlsx",
    sheet_name="Sheet1",
)
df3
df3["Capital"]  # Accessing 'Capital' column from the DataFrame
df3.Capital  # Another way to access 'Capital' column from the DataFrame
df3.loc[111]  # Accessing row with index 111 using loc
df3.iloc[111]  # Accessing row with index 111 using iloc

df4 = pd.read_excel(
    r"C:\Users\deeku\Desktop\Dummy Data\world_population_excel_workbook.xlsx"
)
df4

# 2. Filtering and ordering
df4[df4["Rank"] <= 10]  # Filtering rows where 'Rank' is less than or equal to 10
sepcific_countries = ["India", "China", "United States"]
df4[
    df4["Country"].isin(sepcific_countries)
]  # Filtering rows where 'Country' is in the specified list
df4[
    df4["Country"].str.contains("United")
]  # Filtering rows where 'Country' contains 'United'

# Setting 'Country' as the index of the DataFrame
df5 = df4.set_index("Country")
df5
df5.filter(items=["Rank", "CCA3", "Continent"])  # Filtering specific columns
df5.filter(items=["Yemen"], axis=0)  # Filtering specific rows (axis=0) by index
df5.filter(items=["Yemen"], axis=1)  # Filtering specific columns(axis=1) by index
df5.filter(
    like="C", axis=0
)  # Filtering rows that contain 'C' in their names-countries with name containing 'C'
df5.loc[
    ["India", "China"], ["Rank", "Continent", "2020 Population"]
]  # Accessing specific rows and columns using loc
df5.iloc[[5, 10, 15], [0, 2, 4, 5]]  # Accessing specific rows and columns using iloc

# 3. Sorting
df4[df4["Rank"] <= 10].sort_values(
    by="Rank", ascending=False
)  # Sorting filtered rows by 'Rank' in descending order
df4[df4["Rank"] <= 15].sort_values(by=["Continent", "Country"], ascending=[False, True])

# 4. Indexing and resetting index
df5.reset_index()  # Resetting index to default integer index
df5.reset_index(drop=True)  # Resetting index and dropping the current index
df5.reset_index(
    inplace=True
)  # Resetting index in place without creating a new DataFrame

# Setting 'Country' as index again with/without inplace
df5.set_index("Country")  # setting 'Country' as index again
df5  # setting index is not done inplace so df5 remains same
df5.set_index("Country", inplace=True)  # setting 'Country' as index again with inplace
df5  # now df5 has 'Country' as index

# Multi-level Indexing
df5.set_index(
    ["Continent", "Country"], inplace=True
)  # setting multi-level index with 'Continent' and 'Country' without creating a new dataframe
df5.sort_index(
    ascending=[False, True]
)  # sorting multi-level index first by 'Continent' in descending and then by 'Country' in ascending order
df5
df5.iloc[
    1
]  # iloc can extract row based on position even with multi-level index but not from sorted index
df5.loc[
    ("Asia", "India")
]  # loc needs full index values to extract row with multi-level index
df5.reset_index(inplace=True)
df5

# 5. Group by and agregation
df7 = pd.read_csv(r"C:\Users\deeku\Desktop\Dummy Data\Flavors.csv")
df7
grouped_data = df7.groupby("Base Flavor")
grouped_data.count()  # Counting number of entries in each group
grouped_data.min()  # Finding minimum values in each group
grouped_data.max()  # Finding maximum values in each group
grouped_data.sum()  # Finding sum of values in each group
df7.groupby("Base Flavor").agg(
    {
        "Flavor Rating": ["mean", "max", "min", "sum"],
        "Texture Rating": ["mean", "max", "min", "sum"],
    }
)  # Aggregating multiple functions on multiple columns
df7.groupby("Base Flavor", "Liked").agg(
    {"Falvor Rating": ["mean", "sum", "min", "size", "max"]}
)
