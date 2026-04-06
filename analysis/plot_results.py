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
import matplotlib.pyplot as plt
import pandas as pd

# Variables
__results = pd.read_csv("filename.csv") # for now, a temporary filename is used; the .csv file from runner.py is stored here

# Functions
def display_results_chart():          # Display the results via a DataFrame table
     display(__results)

def plot_random_array_performance():                            # plot the performance of all algorithms for random array distribution
    plt.figure(fig_size = (8, 8))

    # DATA HANDLING GOES HERE
    
    plt.title("Runtime Comparison Chart for Random Array Distribution")         # give the graph a title
    plt.xlabel("n Size")                                                        # give the x-axis (size of array) a title
    plt.ylabel("Runtime")                                                       # give the y-axis (runtime) a title 
    plt.legend()                                                                # give the graph a legend to identify which line represents what

    plt.show()

def plot_nearly_sorted_array_performance():                     # plot the performance of all algorithms for nearly sorted distribution
    plt.figure(fig_size = (8, 8))

    plt.title("Runtime Comparison Chart for Random Array Distribution")
    plt.xlabel("n Size")
    plt.ylabel("Runtime")
    plt.legend()

    plt.show()

def plot_reverse_sorted_array_performance():                    # plot the performance of all algorithms for reverse sorted array distribution
      plt.figure(fig_size = (8, 8))

def plot_duplicates_heavy_array_performance():                  # plot the performance of all algorithms for duplicate-heavy array distribution
      plt.figure(fig_size = (8, 8))

def show_summary_chart_max_n():
