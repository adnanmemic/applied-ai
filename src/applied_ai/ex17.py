import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler

data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["Vineyard"] = data.target
df.to_csv("data/winedata.csv", index=False)
print("data/winedata.csv wurde gespeichert!")

# Dataset
df = pd.read_csv("data/winedata.csv")

# Check for and handle missing values
missing = df.isna().sum()
print("\n=== Missing Values ===")
print(missing)
df.fillna(df.mean(), inplace=True)
print("\nMissing values filled with column mean.")

# Boxplot before normalization
plt.figure(figsize=(12, 6))
sns.boxplot(data=df.drop(columns="Vineyard"))
plt.xticks(rotation=45)
plt.title("Boxplot der Wein-Features (vor Normalisierung)")
plt.xlabel("Features")
plt.ylabel("Wert")
plt.tight_layout()
plt.show()

# Normalization (StandardScaler)
features = df.drop(columns="Vineyard")
scaler = StandardScaler()
scaled_features = pd.DataFrame(scaler.fit_transform(features), columns=features.columns)

# Boxplot after normalization
plt.figure(figsize=(12, 6))
sns.boxplot(data=scaled_features)
plt.xticks(rotation=45)
plt.title("Boxplot der Wein-Features (nach Normalisierung)")
plt.xlabel("Features")
plt.ylabel("Wert (normalisiert)")
plt.tight_layout()
plt.show()
