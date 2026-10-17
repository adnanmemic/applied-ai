import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")

df = pd.read_csv("data/titanic.csv")

df["Sex"] = df["Sex"].replace({"male": "Male", "female": "Female"})

sex_grouped = df.groupby("Sex")
survival_rate = sex_grouped["Survived"].mean().reset_index()

sns.barplot(data=survival_rate, x="Sex", y="Survived")

plt.title("Survival Rate Of Each Sex", fontsize=15, fontweight="bold")
plt.xlabel("Sex")
plt.ylabel("Survival Rate")

plt.ylim(0, 1)  # limits Y-axis between 0 and 1
ax = plt.gca()  # gca = get current axis
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))

plt.show()
