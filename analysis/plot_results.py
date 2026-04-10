#-----------------------------------------------------------------------------------------------------------------------------------
# Purpose:
# 1. Create graphs and a summary chart comparing performances of the four observed algorithms (Insertion Sort, Selection Sort, Quicksort, Mergesort)

# Necessary inputs:
# 1. A .csv file containing the average runtime, std dev, comparison count, and swap count
  # As of now, the .csv file is assumed to have shape () --> (rows, columns)

# Draft of Expected .csv file shape:
#

# Important Information
# 1. There are 4 algorithms, 4 distributions, 6 n-values, and 5 trials per combination (algorithm - distribution - n)



# Outputs and Deliverables
# 1. Singular graph of runtime performances
  # One graph per distribution type (4 total), each distribution has 4 algorithms with varying n
  # x-axis is n, y-axis is runtime
    # find the units of measurement for both
  # REQUIRED: legend, axis labels, title, color consistency

# 2. Summary table of algorithm performances with maximum n inputs
  # can use Pandas DataFrame to cleanly show a table to avoid potential inconsistent formatting; if not use traditional formatting techniques
#-----------------------------------------------------------------------------------------------------------------------------------

# Imports
import os
import matplotlib.pyplot as plt
import pandas as pd

# Consistent color per algorithm across all charts
COLORS = {
    "insertion_sort": "tab:blue",
    "selection_sort": "tab:orange",
    "merge_sort": "tab:green",
    "quicksort": "tab:red",
}

LABELS = {
    "insertion_sort": "Insertion Sort",
    "selection_sort": "Selection Sort",
    "merge_sort": "Merge Sort",
    "quicksort": "Quicksort",
}

RESULTS_CSV = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "experiments", "results", "results.csv"
)

FIGURES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")


def _load_results():
    return pd.read_csv(RESULTS_CSV)


def _save_or_show(fig, filename):
    os.makedirs(FIGURES_DIR, exist_ok=True)
    path = os.path.join(FIGURES_DIR, filename)
    fig.savefig(path, bbox_inches="tight")
    print(f"Saved: {path}")
    plt.close(fig)


def _plot_distribution(df, distribution, title, filename):
    fig, ax = plt.subplots(figsize=(8, 6))
    subset = df[df["distribution"] == distribution].sort_values("n")

    for algo in df["algorithm"].unique():
        algo_data = subset[subset["algorithm"] == algo]
        if algo_data.empty:
            continue
        ax.plot(
            algo_data["n"],
            algo_data["avg_time"],
            marker="o",
            label=LABELS.get(algo, algo),
            color=COLORS.get(algo),
        )

    ax.set_title(title)
    ax.set_xlabel("n (input size)")
    ax.set_ylabel("Average Runtime (seconds)")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    _save_or_show(fig, filename)


def display_results_chart():
    df = _load_results()
    print(df.to_string(index=False))


def plot_random_array_performance():
    df = _load_results()
    _plot_distribution(
        df,
        "random",
        "Runtime Comparison — Random Array Distribution",
        "random_array_performance.png",
    )


def plot_nearly_sorted_array_performance():
    df = _load_results()
    _plot_distribution(
        df,
        "nearly_sorted",
        "Runtime Comparison — Nearly Sorted Array Distribution",
        "nearly_sorted_array_performance.png",
    )


def plot_reverse_sorted_array_performance():
    df = _load_results()
    _plot_distribution(
        df,
        "reverse_sorted",
        "Runtime Comparison — Reverse Sorted Array Distribution",
        "reverse_sorted_array_performance.png",
    )


def plot_duplicates_heavy_array_performance():
    df = _load_results()
    _plot_distribution(
        df,
        "duplicates_heavy",
        "Runtime Comparison — Duplicate-Heavy Array Distribution",
        "duplicates_heavy_array_performance.png",
    )


def show_summary_chart_max_n():
    df = _load_results()

    # For each algorithm, pick the row with the largest n per distribution
    max_n_rows = df.loc[df.groupby(["algorithm", "distribution"])["n"].idxmax()]

    # Pivot: rows = distribution, columns = algorithm, values = avg_time
    pivot = max_n_rows.pivot_table(index="distribution", columns="algorithm", values="avg_time")
    pivot.columns = [LABELS.get(c, c) for c in pivot.columns]

    fig, ax = plt.subplots(figsize=(10, 6))
    pivot.plot(kind="bar", ax=ax, color=[COLORS.get(c.replace(" ", "_").lower(), None) for c in pivot.columns])
    ax.set_title("Summary: Runtime at Maximum n per Distribution")
    ax.set_xlabel("Distribution Type")
    ax.set_ylabel("Average Runtime (seconds)")
    ax.legend(title="Algorithm")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha="right")
    ax.grid(True, axis="y", linestyle="--", alpha=0.5)
    _save_or_show(fig, "summary_max_n.png")


if __name__ == "__main__":
    plot_random_array_performance()
    plot_nearly_sorted_array_performance()
    plot_reverse_sorted_array_performance()
    plot_duplicates_heavy_array_performance()
    show_summary_chart_max_n()
    print("All charts saved to analysis/figures/")
