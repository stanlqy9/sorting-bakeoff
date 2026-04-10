import csv
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort
from algorithms.merge_sort import merge_sort
from algorithms.quicksort import quicksort
from experiments.input_generator import (
    random_array,
    nearly_sorted_array,
    reverse_sorted_array,
    duplicates_heavy_array,
)

TRIALS = 5

ALGORITHMS = {
    "insertion_sort": insertion_sort,
    "selection_sort": selection_sort,
    "merge_sort": merge_sort,
    "quicksort": quicksort,
}

# insertion_sort and selection_sort return (sorted, comparisons, swaps)
# merge_sort and quicksort return (sorted, comparisons)
RETURNS_SWAPS = {"insertion_sort", "selection_sort"}

N_QUADRATIC = [500, 1000, 2000, 5000, 10000, 20000]
N_NLOGN = [1000, 5000, 10000, 50000, 100000, 500000]

DISTRIBUTIONS = {
    "random": random_array,
    "nearly_sorted": nearly_sorted_array,
    "reverse_sorted": reverse_sorted_array,
    "duplicates_heavy": duplicates_heavy_array,
}


def run_benchmarks():
    results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(results_dir, exist_ok=True)

    rows = []

    for algo_name, algo_fn in ALGORITHMS.items():
        n_values = N_QUADRATIC if algo_name in RETURNS_SWAPS else N_NLOGN

        for dist_name, gen_fn in DISTRIBUTIONS.items():
            for n in n_values:
                times = []
                comparisons_list = []
                swaps_list = []

                for _ in range(TRIALS):
                    arr = gen_fn(n)  # generate input before timing

                    start = time.perf_counter()
                    result = algo_fn(arr)
                    elapsed = time.perf_counter() - start

                    times.append(elapsed)

                    if algo_name in RETURNS_SWAPS:
                        _, comparisons, swaps = result
                        comparisons_list.append(comparisons)
                        swaps_list.append(swaps)
                    else:
                        _, comparisons = result
                        comparisons_list.append(comparisons)

                avg_time = sum(times) / TRIALS
                std_time = (sum((t - avg_time) ** 2 for t in times) / TRIALS) ** 0.5
                avg_comparisons = sum(comparisons_list) / TRIALS
                avg_swaps = sum(swaps_list) / TRIALS if swaps_list else ""

                rows.append({
                    "algorithm": algo_name,
                    "distribution": dist_name,
                    "n": n,
                    "avg_time": avg_time,
                    "std_time": std_time,
                    "avg_comparisons": avg_comparisons,
                    "avg_swaps": avg_swaps,
                })

                print(f"{algo_name} | {dist_name} | n={n}: {avg_time:.6f}s")

    csv_path = os.path.join(results_dir, "results.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["algorithm", "distribution", "n", "avg_time", "std_time", "avg_comparisons", "avg_swaps"],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nResults written to {csv_path}")


if __name__ == "__main__":
    run_benchmarks()
