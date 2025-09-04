import pandas as pd
import os

directory_current = os.path.dirname(os.path.abspath(__file__))
route_file = os.path.join(directory_current, "data.csv")

with open(route_file, "r", encoding="cp1252") as file:
    df = pd.read_csv(file, header=None, names=["Name", "Age", "City"])
"""     for index, row in df.iterrows():
        print(f"Row {index}: {row.to_dict()}") """
# delete only nan
df = df.dropna(subset=["Age"])

# delete duplicate
df = df.drop_duplicates(subset=["Name"])

# reset index so loc[2] exists
df = df.reset_index(drop=True)

# cast Age to int
df["Age"] = df["Age"].astype(int)

# oldest person
old = df.sort_values(by="Age", ascending=False).head(1).values[0]

# update name in row 2
NewName = df.loc[2, "Name"] = "jose"

# replace city
df["City"] = df["City"].replace("Bucaramanga", "Medellin")


# save to new csv
new_route_file = os.path.join(directory_current, "data_cleaned.csv")
df.to_csv(new_route_file, index=False)

print(df)

print(
    f"The oldest person is {old[0]}, who is {old[1]} years old and lives in {old[2]}."
)
print(f"The second person is {NewName} and lives in {df.loc[2, 'City']}.")
