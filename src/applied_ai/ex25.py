
import pandas as pd

# Load the dataset
df = pd.read_csv("data/restaurant.csv", sep=";")

target = "Will Wait (Y)"

features = [
    "Alternate", "Bar", "Fri/Sat", "Hungry", "Patrons",
    "Price", "Rain", "Reservation", "Type", "WaitEstimate"
]


# Calculate the Gini impurity
def gini(series):
    p = series.value_counts(normalize=True)
    return (p * (1 - p)).sum()


# Calculate the weighted Gini impurity for a feature
def gini_split(df, feature):
    total = len(df)

    return sum(
        (len(group) / total) * gini(group[target])
        for _, group in df.groupby(feature)
    )


# Build the decision tree recursively
def build_tree(df, features, depth=0):
    indent = "    " * depth

    # Count the occurrences of each target class
    counts = df[target].value_counts()

    # Create a leaf if all samples belong to the same class
    if len(counts) == 1:
        result = counts.index[0]
        print(f"{indent}=> {result}")
        return result

    # Use the majority class if no features remain
    if not features:
        result = counts.idxmax()
        print(f"{indent}=> {result} (majority)")
        return result

    # Calculate Gini values for all remaining features
    results = {
        feature: gini_split(df, feature)
        for feature in features
    }

    print(f"\n{indent}Gini values:")

    for feature, value in results.items():
        print(f"{indent}{feature}: {value:.4f}")

    # Select the feature with the lowest Gini impurity
    best_feature = min(results, key=results.get)

    print(f"{indent}Best feature: {best_feature}")

    # Remove the selected feature from the remaining features
    remaining_features = [
        feature for feature in features
        if feature != best_feature
    ]

    tree = {best_feature: {}}

    # Recursively split the dataset for each feature value
    for value, group in df.groupby(best_feature):
        print(f"\n{indent}{best_feature} = {value}")
        print(f"{indent}Samples: {len(group)}")
        print(f"{indent}Gini: {gini(group[target]):.4f}")
        print(group[target].value_counts())

        subtree = build_tree(
            group,
            remaining_features,
            depth + 1
        )

        tree[best_feature][value] = subtree

    return tree


# Build the complete decision tree
print("=== Decision Tree with Gini Index ===")

tree = build_tree(df, features)

# Display the final decision tree
print("\n=== Final Decision Tree ===")
print(tree)
