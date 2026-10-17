import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data/titanic.csv")

df_flow = df[["Embarked", "Survived"]].dropna()

# change values to full names
port_names = {"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"}
df_flow["embarked_name"] = df_flow["Embarked"].map(port_names)

surv_names = {0: "Died", 1: "Survived"}
df_flow["survived_name"] = df_flow["Survived"].map(surv_names)

# data frame: embarked_name | survived_name | count (before: index)
flow = (
    df_flow.groupby(["embarked_name", "survived_name"]).size().reset_index(name="count")
)

nodes = list(port_names.values()) + list(surv_names.values())
node_index = {name: i for i, name in enumerate(nodes)}

flow["source"] = flow["embarked_name"].map(node_index)
flow["target"] = flow["survived_name"].map(node_index)

# sankey diagram
fig = go.Figure(
    data=[
        go.Sankey(
            node={"pad": 20, "thickness": 20, "label": nodes},
            link={
                "source": flow["source"],
                "target": flow["target"],
                "value": flow["count"],
            },
        )
    ]
)

fig.update_layout(
    title_text="Titanic passenger flow: Embarkation → Survival", font_size=12
)

fig.show()
