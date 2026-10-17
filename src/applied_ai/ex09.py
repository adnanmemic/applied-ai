import pandas as pd

df = pd.read_csv("data/titanic.csv")

# All people that have embarked in Southampton
data = df["Embarked"].value_counts()["S"]  # no empty row
print(f"Amount of people embarked in Southampton: {data}")

# Highest fare
max_fare = df["Fare"].max()
df_maxFare = df[df["Fare"] == max_fare]
print(df_maxFare["Name"])

# Youngest Passenger
min_age = df["Age"].min()
min_age_df = df[df["Age"] == min_age]
print(min_age_df[["Name", "Age"]])

# Oldest Passenger who died during the trip
unsurvived_df = df[df["Survived"] == 0]  # first get the people who did not survive
oldest_unsurviver_df = unsurvived_df[
    unsurvived_df["Age"] == unsurvived_df["Age"].max()
]  # then get the oldest of them
print(oldest_unsurviver_df[["Name", "Age"]])
