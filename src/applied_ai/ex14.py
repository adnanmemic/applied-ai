import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import seaborn as sns

country_name = "Austria"

sns.set_theme(style="whitegrid")

world = pd.read_csv("data/internet_usage.csv", skiprows=3)

# case insensitive column names
world.columns = world.columns.str.lower()

# get country details
country = world[world["country name"] == country_name]

# make a list of the year columns
years = [x for x in country.columns if x.isdigit()]

country_new = country.melt(
    id_vars="country name",  # columns that are not going to be changed
    value_vars=years,  # columns that are going to be converted to a row
    var_name="year",  # column name of the rows
    value_name="internet_usage",  # values from the old columns
)

sns.lineplot(data=country_new, x="year", y="internet_usage")

plt.title(f"Internet Usage in {country_name} Over Time", fontsize=15, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Internet Usage")
# automatically adjusts spacing to ensure that the map and the colorbar fit in the figure
plt.tight_layout()
plt.ylim(0, 100)

ax = plt.gca()  # gca = get current axis
ax.yaxis.set_major_formatter(mtick.PercentFormatter(100))

plt.show()
