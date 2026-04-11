#-----------------------------------------------------------------------------------------------------------------------------------
# Purpose:
# 1. Create graphs and a summary chart comparing performances of the four observed algorithms (Insertion Sort, Selection Sort, Quicksort, Mergesort)

# Necessary inputs:
# 1. A .csv file containing the average runtime, std dev, comparison count, and swap count
  # As of now, the .csv file is assumed to have shape () --> (rows, columns)

# Necessary libraries
# pandas --> for data loading, .csv file management
# matplotlib --> for graph creation
# IPython --> primarily to use the display() function, this is a shell

# Important Information
# 1. Expected 96 rows (4 distributions * 4 algorithms * 6 sizes = 96 unique combos)

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
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display

# Variables
__results = pd.read_csv("mock_data_sortingbakeoff.csv") # for now, a temporary filename is used; the .csv file from runner.py is stored here

# Functions
def display_results_chart():          # Display the results via a DataFrame table
    print("Results of All Algorithms for All Distributions at Varying n Sizes")
    print("------------------------------------------------------------------")
    display(__results)

def plot_random_array_performance():                            # plot the performance of all algorithms for random array distributions
    rand_array_rows = __results.loc[__results["Distribution"] == "Random Array"] # grab all rows that are of random array distribution

    alg_types = rand_array_rows["Algorithm"].unique() # get an array of all algorithm types

    # Choose graph size
    plt.figure(figsize = (15, 10))
    
    for current_alg in alg_types: # iterate through all algorithms available
        current_sort = rand_array_rows.loc[rand_array_rows["Algorithm"] == current_alg]
        plt.plot(current_sort["n"], current_sort["Avg Time (sec)"], marker = "o", label = current_alg)
    
    # Graph components
    plt.title("Random Array Distribution: Average Time vs. n")  # give the graph a title
    plt.xlabel("n Size")                                        # give the x-axis (size of array) a title
    plt.ylabel("Average Runtime (sec)")                                       # give the y-axis (runtime) a title 
    plt.legend()                                                # give the graph a legend to identify which line represents what,
                                                                # it uses label from plt.plot(...) to make the legend
    
    # Display graph
    plt.show()

def plot_nearly_sorted_array_performance():                     # plot the performance of all algorithms for nearly sorted distribution
    nearly_sorted_array_rows = __results.loc[__results["Distribution"] == "Nearly Sorted Array"]

    alg_types = nearly_sorted_array_rows["Algorithm"].unique()

    # Choose graph size
    plt.figure(figsize = (15, 10))

    for current_alg in alg_types:
        current_sort = nearly_sorted_array_rows.loc[nearly_sorted_array_rows["Algorithm"] == current_alg]
        plt.plot(current_sort["n"], current_sort["Avg Time (sec)"], marker = "o", label = current_alg)
        
    plt.title("Nearly Sorted Array Distribution: Average Time vs. n")
    plt.xlabel("n Size")
    plt.ylabel("Average Runtime (sec)")
    plt.legend()

    plt.show()
    
def plot_reverse_sorted_array_performance():                    # plot the performance of all algorithms for reverse sorted array distribution
    reverse_sorted_array_rows = __results.loc[__results["Distribution"] == "Reverse Sorted Array"]

    alg_types = reverse_sorted_array_rows["Algorithm"].unique()

    # Choose graph size
    plt.figure(figsize = (15, 10))

    for current_alg in alg_types:
        current_sort = reverse_sorted_array_rows.loc[reverse_sorted_array_rows["Algorithm"] == current_alg]
        plt.plot(current_sort["n"], current_sort["Avg Time (sec)"], marker = "o", label = current_alg)

    plt.title("Reverse Sorted Array Distribution: Average Time vs. n")
    plt.xlabel("n Size")
    plt.ylabel("Average Runtime (sec)")
    plt.legend()

    plt.show()
    
def plot_duplicates_heavy_array_performance():                  # plot the performance of all algorithms for duplicate-heavy array distribution
    dup_heavy_array_rows = __results.loc[__results["Distribution"] == "Duplicate Heavy Array"]

    alg_types = dup_heavy_array_rows["Algorithm"].unique()

    # Choose graph size
    plt.figure(figsize = (15, 10))

    for current_alg in alg_types:
        current_sort = dup_heavy_array_rows.loc[dup_heavy_array_rows["Algorithm"] == current_alg]
        plt.plot(current_sort["n"], current_sort["Avg Time (sec)"], marker = "o", label = current_alg)

    plt.title("Duplicate Heavy Array Distribution: Average Time vs. n")
    plt.xlabel("n Size")
    plt.ylabel("Average Runtime (sec)")
    plt.legend()

    plt.show()

def show_summary_chart_max_n():
    alg_types = __results["Algorithm"].unique() # grab all unique algorithm types (4 expected ones)
    dist_types = __results["Distribution"].unique() # grab all unique distribution types (4 expected ones)

    rows_max_n = [] # store data points with max n size here
    
    for current_alg in alg_types: # iterate through all algorithms
        alg_rows = __results.loc[__results["Algorithm"] == current_alg] # filter for the current algorithm
        for current_dist in dist_types: # iterate through all distributions per algorithm
            dist_rows = alg_rows.loc[alg_rows["Distribution"] == current_dist] # filter for the current distribution
            max_n_row = dist_rows.loc[dist_rows["n"] == dist_rows["n"].max()] # get the max n row
            rows_max_n.append(max_n_row)

    chart_max_n = pd.concat(rows_max_n, ignore_index = True) # turn the rows into a DataFrame (data table)
    
    print("Summary Chart of All Algorithms for All Distribution Types at Max n Size")
    print("------------------------------------------------------------------------")
    display(chart_max_n)
  

# Other Version
'''
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
'''
