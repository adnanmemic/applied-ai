import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree

# Generate the training data
num_points = 80
interval_dist = 3

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(num_points, 1), axis=0)
y = np.sin(X).ravel()

y[::interval_dist] += 3 * (
    0.5 - rng.rand(int(np.ceil(num_points / interval_dist)))
)

# Generate test data across the training range
X_test = np.linspace(X.min(), X.max(), 500).reshape(-1, 1)

# Create regression trees with different maximum depths
tree_depth_2 = DecisionTreeRegressor(max_depth=2, random_state=0)
tree_depth_5 = DecisionTreeRegressor(max_depth=5, random_state=0)

# Train the regression trees
tree_depth_2.fit(X, y)
tree_depth_5.fit(X, y)

# Create a pruned regression tree
tree_pruned = DecisionTreeRegressor(
    max_depth=5,
    ccp_alpha=0.05,
    random_state=0
)
tree_pruned.fit(X, y)

# Predict the test values
y_depth_2 = tree_depth_2.predict(X_test)
y_depth_5 = tree_depth_5.predict(X_test)
y_pruned = tree_pruned.predict(X_test)

# Compare the predictions
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

models = [
    ("Max Depth = 2", y_depth_2),
    ("Max Depth = 5", y_depth_5),
    ("Pruned Tree (ccp_alpha = 0.05)", y_pruned)
]

for ax, (title, prediction) in zip(axes, models):
    ax.scatter(X, y, color="black", label="Training Data")
    ax.plot(X_test, prediction, color="red", label="Prediction")
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("y")
    ax.legend()

plt.tight_layout()
plt.show()

# Compare tree depths and leaf counts
print("Tree Comparison:")

for name, model in [
    ("Depth 2", tree_depth_2),
    ("Depth 5", tree_depth_5),
    ("Pruned", tree_pruned)
]:
    print(
        f"{name}: "
        f"Depth = {model.get_depth()}, "
        f"Leaves = {model.get_n_leaves()}"
    )

# Compare different pruning strengths
print("\nPruning Comparison:")

for alpha in [0.0, 0.01, 0.05, 0.1, 0.2]:
    model = DecisionTreeRegressor(
        max_depth=5,
        ccp_alpha=alpha,
        random_state=0
    )
    model.fit(X, y)

    print(
        f"ccp_alpha = {alpha}: "
        f"Depth = {model.get_depth()}, "
        f"Leaves = {model.get_n_leaves()}"
    )

# Visualize the decision trees
fig, axes = plt.subplots(3, 1, figsize=(18, 16))

for ax, (title, model) in zip(
    axes,
    [
        ("Regression Tree - Depth 2", tree_depth_2),
        ("Regression Tree - Depth 5", tree_depth_5),
        ("Pruned Regression Tree", tree_pruned)
    ]
):
    plot_tree(
        model,
        ax=ax,
        filled=True,
        rounded=True,
        fontsize=7
    )
    ax.set_title(title)

plt.tight_layout()
plt.show()
