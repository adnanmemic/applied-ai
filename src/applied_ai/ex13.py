import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

world = gpd.read_file("data/110m_cultural/ne_110m_admin_0_countries.shp")
internet = pd.read_csv(
    "data/internet_usage.csv", skiprows=3
)  # to read the csv properly skip the header

# case insensitive
world.columns = world.columns.str.lower()  # convert column names to lowercase
world["continent"] = world[
    "continent"
].str.lower()  # all values from 'column' to lowercase
internet.columns = internet.columns.str.lower()

# merge both dataframes
world_internet = world.merge(internet, left_on="adm0_a3", right_on="country code")

# filtering just the countries located in asia
asia = world_internet[world_internet["continent"] == "asia"]

asia.plot(
    column="2015",
    cmap="viridis",  # colors
    edgecolor="black",  # lines of countries
    linewidth=0.5,
    legend=True,
    legend_kwds={
        "label": "Internet users (% of population)",
        "orientation": "vertical",
    },
)

plt.title("Internet Usage in Asia (2015)", fontsize=15, fontweight="bold")
# automatically adjusts spacing to ensure that the map and the colorbar fit in the figure
plt.tight_layout()
plt.show()
