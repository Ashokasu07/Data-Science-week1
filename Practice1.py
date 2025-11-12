import pandas as pd

df = pd.read_excel(r"C:\Users\deeku\Desktop\Dummy Data\Customer Call List.xlsx")
df.head()

# Removing Duplicates
df = df.drop_duplicates()
df.info()

# Dropping unnecessary column
df = df.drop(columns="Not_Useful_Column")

# Stripping unwanted characters from Last_Name column
df["Last_Name"] = df["Last_Name"].str.strip("123./_!@#$%^&*()")
df

# Cleaning Phone_Number column
df["Phone_Number"] = df["Phone_Number"].str.replace("[^a-zA-Z0-9]", "", regex=True)
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))  # Converting to string
df["Phone_Number"] = df["Phone_Number"].apply(
    lambda x: x[0:3] + "-" + x[3:6] + "-" + x[6:]
)  # Formatting
df["Phone_Number"] = df["Phone_Number"].str.replace("nan--", "")
df["Phone_Number"] = df["Phone_Number"].str.replace("Na--", "")
df

# Cleaning Address column
df[["Street", "State", "Zip_Code"]] = df["Address"].str.split(",", expand=True)
df

# Cleaning Paying Customer and Do_Not_Contact columns
df["Paying Customer"] = df["Paying Customer"].str.replace("Yes", "Y")
df["Paying Customer"] = df["Paying Customer"].str.replace("No", "N")
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes", "Y")
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("No", "N")
df

# Final cleaning dataframe
df = df.fillna("")
df

# Taking out the data that needs to be contacted
for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == "Y":
        df.drop(x, inplace=True)
    if (
        df.loc[x, "Phone_Number"] == ""
    ):  # Another way: df.dropna(subset=["Phone_Number"], inplace=True)
        df.drop(x, inplace=True)

df.reset_index(drop=True, inplace=True)
df
