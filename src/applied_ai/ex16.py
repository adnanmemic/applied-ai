import pandas as pd
from sklearn.datasets import load_wine

wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)

# shape and column
print(f"Rows And Columns: {df.shape} \n")
print(f"Columns: {df.columns}\n")

# description
print(f"Description:\n{df.describe()} \n")

# missing values
empty_values = df.isnull().sum().sum()
print(f"Empty Values: {empty_values} \n")

df.to_csv("wine.csv", index=False)
print(df)
