import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    BaggingClassifier,
    AdaBoostClassifier
)

# Generate a linearly separable dataset
X, y = make_classification(
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=1,
    n_clusters_per_class=1
)

# Add random noise to the dataset
rng = np.random.RandomState(2)
X += 2 * rng.uniform(size=X.shape)

linear_separable = (X, y)

# Create the three datasets
datasets = [
    make_moons(noise=0.3, random_state=0),
    make_circles(noise=0.2, factor=0.5, random_state=1),
    linear_separable
]

dataset_names = [
    "Moons",
    "Circles",
    "Linearly Separable"
]

# Create the classifiers
classifiers = [
    DecisionTreeClassifier(random_state=0),
    RandomForestClassifier(n_estimators=100, random_state=0),
    BaggingClassifier(n_estimators=100, random_state=0),
    AdaBoostClassifier(n_estimators=100, random_state=0)
]

classifier_names = [
    "Decision Tree",
    "Random Forest",
    "Bagging",
    "AdaBoost"
]

# Create a grid of plots
fig, axes = plt.subplots(3, 4, figsize=(18, 12))

# Train and visualize each classifier on each dataset
for row, ((X, y), dataset_name) in enumerate(zip(datasets, dataset_names)):

    # Create a mesh grid covering the feature space
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 200),
        np.linspace(y_min, y_max, 200)
    )

    grid = np.c_[xx.ravel(), yy.ravel()]

    for col, (classifier, classifier_name) in enumerate(
        zip(classifiers, classifier_names)
    ):
        ax = axes[row, col]

        # Train the classifier
        classifier.fit(X, y)

        # Predict class probabilities for the mesh grid
        probabilities = classifier.predict_proba(grid)[:, 1]
        probabilities = probabilities.reshape(xx.shape)

        # Visualize the decision regions
        ax.contourf(
            xx,
            yy,
            probabilities,
            levels=np.linspace(0, 1, 11),
            cmap="RdBu",
            alpha=0.7,
            vmin=0,
            vmax=1
        )

        # Draw the decision boundary at probability 0.5
        ax.contour(
            xx,
            yy,
            probabilities,
            levels=[0.5],
            colors="black",
            linewidths=1
        )

        # Plot the original data points
        ax.scatter(
            X[:, 0],
            X[:, 1],
            c=y,
            cmap="RdBu",
            edgecolors="black",
            s=25
        )

        ax.set_title(f"{dataset_name} - {classifier_name}")
        ax.set_xlabel("Feature 1")
        ax.set_ylabel("Feature 2")

plt.tight_layout()
plt.show()
