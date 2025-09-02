import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

directory_current = os.path.dirname(os.path.abspath(__file__))
route_file = os.path.join(directory_current, "cofla.csv")

df = pd.read_csv(route_file, header=0, usecols=["fuentes", "Ingreso"])

print(df)
sns.barplot(x="fuentes", y="Ingreso", data=df)

total = df["Ingreso"].sum()
print(f"Total Ingreso: {total}")

# show
plt.show()
