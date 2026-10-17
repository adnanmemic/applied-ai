import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")

url = "https://raw.githubusercontent.com/ADSLab-Salzburg/DataAnalysiswithPython/refs/heads/main/data/opsd_germany_daily.csv"
df = pd.read_csv(url)

fig, axs = plt.subplots(3, 1)  # 3 rows, 1 column

df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

# daily consumption
axs[0].plot(df.index, df["Consumption"])
axs[0].set_title("Daily Energy Consumption")
axs[0].set_ylabel("Energie GWh")

# daily solar generation
axs[1].plot(df.index, df["Solar"], color="orange")
axs[1].set_title("Daily Solar Generation")
axs[1].set_ylabel("Energie GWh")

# daily wind generation
axs[2].plot(df.index, df["Wind"], color="green")
axs[2].set_title("Daily Wind Generation")
axs[2].set_ylabel("Energie GWh")

plt.xlabel("Year")
plt.tight_layout()

plt.show()
