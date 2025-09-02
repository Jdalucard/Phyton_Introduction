import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

directory_current = os.path.dirname(os.path.abspath(__file__))
route_file = os.path.join(directory_current, "problem.csv")

df = pd.read_csv(route_file, header=0, parse_dates=["date"], dayfirst=True)

sns.lineplot(x="date", y="problem", data=df, marker="o")

plt.plot(df["date"], df["problem"], marker="o")


plt.show()
