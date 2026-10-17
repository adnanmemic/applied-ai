import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/winedata.csv")
df.fillna(df.mean(), inplace=True)

# StandardScaler
scaler = StandardScaler()
scaled_df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# PCA to reduce to 2 dimensions
pca = PCA(n_components=2)  # Reduce from 13 features to 2 principal components
reduced = pca.fit_transform(scaled_df)  # Compute components and transform the data
reduced_df = pd.DataFrame(
    reduced, columns=["Dim1", "Dim2"]
)  # Create a DataFrame with 2 columns

# Scatter plot (no labels provided)
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Dim1", y="Dim2", data=reduced_df)
plt.title("PCA Dimensionality Reduction")
plt.show()
