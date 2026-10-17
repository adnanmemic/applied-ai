import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")  # Show grid lines

url = "https://raw.githubusercontent.com/ADSLab-Salzburg/DataAnalysiswithPython/refs/heads/main/data/opsd_germany_daily.csv"
df = pd.read_csv(url)  # Read the CSV file into a DataFrame

print(f"Head: \n{df.head()}")  # Display the first 5 rows
print()
print(
    f"Beschreibung: \n{df.describe()}"
)  # Show summary statistics such as minimum and maximum
print()
print(f"Type: \n{df.dtypes}")  # Show the data type of each column

df["Date"] = pd.to_datetime(
    df["Date"]
)  # Convert strings in the "Date" column to datetime objects

df = df.set_index("Date")  # Use Date as the index

# Create three new columns: Year, Month, and Day
df["Year"] = df.index.year
df["Month"] = df.index.month
df["Day"] = df.index.day_name()  # Use weekday names as values

sns.lineplot(df, x=df.index, y=df["Consumption"])  # Line chart
plt.xlabel("Year")
plt.ylabel("Energie in GWh")

plt.show()
