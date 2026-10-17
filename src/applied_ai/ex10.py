import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

sns.set_theme(style="whitegrid")

df = pd.read_csv('data/titanic.csv')

class_group = df.groupby('Pclass') # axis values are the name of the name of the group

survival_rate = class_group['Survived'].mean().reset_index() # reset index to get a dataframe instead of series

sns.barplot(
    data=survival_rate,
    x='Pclass',
    y='Survived'
)

plt.title(
    'Survival Rate by Passenger Class',
    fontsize=15,
    fontweight='bold'
)
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')

plt.ylim(0, 1)  # Y-axis between 0 and 1
ax = plt.gca() # gca = get current axis
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0)) # Format the Y-Axis major ticks as percentage

plt.show()
