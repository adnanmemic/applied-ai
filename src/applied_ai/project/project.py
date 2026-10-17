from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", font_scale=1.1)

# Configs
SEPERATOR = "=" * 70

ATHLETE_EVENTS_FILE = "./data/athlete-events.csv"
NOC_REGIONS_FILE = "./data/noc-regions.csv"
OUTPUT_DIR = "plots"

FOCUS_NOC = "USA"        
FOCUS_SPORT = None      # example "Swimming"
FOCUS_SEASON = None     # example "Summer"

TOP_K_SPORTS = 11        # number of sports for boxplot

NO_GOLD_COLOR = "orange"
GOLD_COLOR = "steelblue"

PLOTA = "plot-A-gold-vs-nongold-hist.png"
PLOTB = "plot-B-time-series-gold-vs-nongold.png"
PLOTC = "plot-C-box-by-sport-gold.png"


# Load data
def load_and_merge():
    athletes = pd.read_csv(ATHLETE_EVENTS_FILE)
    noc = pd.read_csv(NOC_REGIONS_FILE)
    return athletes.merge(noc, on="NOC", how="left")


# Filter data so its only valid ages and set filter mode
def filter_base(df):
    sub = df.copy()

    # valid age
    sub["Age"] = pd.to_numeric(sub["Age"], errors="coerce") # converts non numeric values into numeric, if not possible then NAN
    sub = sub[sub["Age"].notna()].copy()
    sub = sub[(sub["Age"] >= 10) & (sub["Age"] <= 80)].copy() # Filter Age between 10 and 80

    # Filter mode 
    if FOCUS_NOC:
        sub = sub[sub["NOC"] == FOCUS_NOC].copy()
    if FOCUS_SPORT:
        sub = sub[sub["Sport"] == FOCUS_SPORT].copy()
    if FOCUS_SEASON:
        sub = sub[sub["Season"] == FOCUS_SEASON].copy()

    return sub


# Add Column "Gold" (Values: true/false)
def add_is_gold_flag(df_base):
    out = df_base.copy()
    out["IsGold"] = (out["Medal"] == "Gold") 
    return out


# Filter people that have gold medals
def get_gold_only(df_base):
    return df_base[df_base["Medal"] == "Gold"].copy() 


# Make title prefix based on filter mode
def build_title_prefix():
    parts = []
    if FOCUS_NOC:
        parts.append(FOCUS_NOC)
    if FOCUS_SEASON:
        parts.append(FOCUS_SEASON)
    if FOCUS_SPORT:
        parts.append(FOCUS_SPORT)
    return " | ".join(parts) if parts else "All"


# Plot A — Histogram: Gold vs No-Gold
def plot_A_gold_vs_nongold_hist(df_labeled, out_dir, title_prefix):
    plt.figure(figsize=(8, 5))

    sns.histplot(
        df_labeled[df_labeled["IsGold"] == False]["Age"],
        bins=30,
        stat="count",
        label="No Gold",
        color=NO_GOLD_COLOR,
        alpha=1
    )

    sns.histplot(
        df_labeled[df_labeled["IsGold"] == True]["Age"],
        bins=30,
        stat="count",
        label="Gold",
        color=GOLD_COLOR,
        alpha=1
    )

    plt.title(f"{title_prefix}: Age distribution (Gold vs No Gold)")
    plt.xlabel("Age")
    plt.ylabel("Number of people")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_dir / PLOTA, dpi=200)
    plt.close()


# Plot B — Line plot: Mean age over time (Gold vs No-Gold)
def plot_B_time_series_gold_vs_nongold(df_labeled, out_dir, title_prefix):
    gold = df_labeled[df_labeled["IsGold"]].groupby("Year")["Age"].mean().reset_index()
    nongold = df_labeled[~df_labeled["IsGold"]].groupby("Year")["Age"].mean().reset_index()

    gold["Group"] = "Gold"
    nongold["Group"] = "No Gold"

    data = pd.concat([gold, nongold])

    # legend order to "No Goal" first 
    data["Group"] = pd.Categorical(
        data["Group"],
        categories=["No Gold", "Gold"],
        ordered=True
    )

    plt.figure(figsize=(9, 5))

    sns.lineplot(
        data=data,
        x="Year",
        y="Age",
        hue="Group",
        linewidth=2.5,
        palette={
            "Gold": GOLD_COLOR,
            "No Gold": NO_GOLD_COLOR
        }
    )

    plt.title(f"{title_prefix}: Mean age over time (Gold vs No Gold)")
    plt.xlabel("Year")
    plt.ylabel("Mean age")
    plt.tight_layout()
    plt.savefig(out_dir / PLOTB, dpi=200)
    plt.close()


# Plot C — Boxplot: Gold medalists age by sport (top K sports)
def plot_C_box_by_sport_gold(df_gold, out_dir, title_prefix, top_k):
    top_sports = df_gold["Sport"].value_counts().head(top_k).index
    sub = df_gold[df_gold["Sport"].isin(top_sports)].copy()

    plt.figure(figsize=(12, 6))

    sns.boxplot(
        data=sub,
        x="Sport",
        y="Age",
        order=top_sports,
        showfliers=False,
        color=GOLD_COLOR
    )

    plt.title(f"{title_prefix}: Gold medalists age by sport (Top {top_k})")
    plt.xlabel("Sport")
    plt.ylabel("Age")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(out_dir / PLOTC, dpi=200)
    plt.close()


def main():
    # Output directory
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(exist_ok=True)

    # Data loading 
    print("\nLoading data...")
    df = load_and_merge()
    if df.empty:
        raise ValueError("Loaded dataframe is empty!")
    else:
        print("-> Data loaded successfully!")
        print(SEPERATOR)

    # Data filtering 
    print("Filtering data...")
    df_base = filter_base(df)
    if df_base.empty:
        raise ValueError("No rows left after filtering!")
    else:
        print("-> Data filtered successfully!")
        print(SEPERATOR)
        
    # Add Column "Gold"
    df_labeled = add_is_gold_flag(df_base)

    # Filter people that have gold
    df_gold = get_gold_only(df_base)

    print("Gold rows:", int(df_labeled["IsGold"].sum()))
    print("Non-gold rows:", int((~df_labeled["IsGold"]).sum()))
    print("Total:", len(df_base))
    print(SEPERATOR)

    # Title prefix for the titles of the plots
    title_prefix = build_title_prefix()

    # Create plots
    print("Creating Plots...")
    plot_A_gold_vs_nongold_hist(df_labeled, out_dir, title_prefix)
    plot_B_time_series_gold_vs_nongold(df_labeled, out_dir, title_prefix)
    plot_C_box_by_sport_gold(df_gold, out_dir, title_prefix, TOP_K_SPORTS)
    print("Plots saved to:", out_dir.resolve())
    print("Generated:")
    print(f"- {PLOTA}")
    print(f"- {PLOTB}")
    print(f"- {PLOTC}\n")


if __name__ == "__main__":
    main()