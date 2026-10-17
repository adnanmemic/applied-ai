import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree

# Load the dataset
df = pd.read_csv("data/restaurant.csv", sep=";")

# Define the target variable
y = df["Will Wait (Y)"].map({"Yes": 1, "No": 0})

# Select the input features
X = df.drop(columns=["Example", "Will Wait (Y)"])

# Convert categorical features into numerical values
X_encoded = pd.get_dummies(X)

print("Feature Matrix:")
print(X_encoded.head())

print("\nTarget Labels:")
print(y.head())

# Create the decision tree classifier using the Gini index
tree_clf = DecisionTreeClassifier(criterion="gini", random_state=0)

# Train the model
tree_clf.fit(X_encoded, y)

# Display the decision tree as text
tree_rules = export_text(tree_clf, feature_names=list(X_encoded.columns))

print("\nDecision Tree Rules:")
print(tree_rules)

# Visualize the decision tree
plt.figure(figsize=(14, 8))

plot_tree(
    tree_clf,
    feature_names=list(X_encoded.columns),
    class_names=["No", "Yes"],
    filled=True,
    rounded=True,
)

plt.tight_layout()
plt.show()
