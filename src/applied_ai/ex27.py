import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_circles, make_classification, make_moons

# Generate a linearly separable dataset
X, y = make_classification(
    n_features=2, n_redundant=0, n_informative=2, random_state=1, n_clusters_per_class=1
)

# Add random noise to the dataset
rng = np.random.RandomState(2)
X += 2 * rng.uniform(size=X.shape)

linear_separable = (X, y)

# Create the three datasets
datasets = [
    make_moons(noise=0.3, random_state=0),
    make_circles(noise=0.2, factor=0.5, random_state=1),
    linear_separable,
]

names = ["Moons", "Circles", "Linearly Separable"]

# Create a figure with three plots
plt.figure(figsize=(12, 4))

# Visualize each dataset in two dimensions
for i, ((X, y), name) in enumerate(zip(datasets, names)):
    plt.subplot(1, 3, i + 1)

    # Plot the two features and color points by class
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", edgecolors="black")

    plt.title(name)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")

plt.tight_layout()
plt.show()
