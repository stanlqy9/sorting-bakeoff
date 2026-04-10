# Sorting Algorithm Bake-Off

Final group project for [CSC-401] — Spring, 2026

## Team Members
- Stanley Navarrete
- Danya Leyva
- Joel Linares
- Alejandro Garcia
- Kristopher Manalang
- Avishek Barua

## Project Overview
A comparison of sorting algorithms (Insertion Sort, Selection Sort, Merge Sort, Quicksort)
across different input types and sizes. We analyze theoretical complexity and validate
it through empirical benchmarking.

## Topic
**Topic #6** — Sorting Algorithm Bake-Off  
Baseline: Insertion Sort, Selection Sort → Θ(n²)  
Improved: Merge Sort → Θ(n log n), Quicksort → avg Θ(n log n)

---

## Installation

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv path/to/venv
   source path/to/venv/bin/activate  # macOS/Linux
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Experiments

From the project root, run:

```bash
python experiments/runner.py
```

This benchmarks all four algorithms across all four input distributions and writes results to `experiments/results/results.csv`.

---

## Reproducing the Charts

After running the experiments, generate all charts with:

```bash
python analysis/plot_results.py
```

Charts are saved to `analysis/figures/`:
- `random_array_performance.png`
- `nearly_sorted_array_performance.png`
- `reverse_sorted_array_performance.png`
- `duplicates_heavy_array_performance.png`
- `summary_max_n.png`

---

## Running the Tests

```bash
pytest tests/test_sorts.py
```

---

## File and Function Reference

### `algorithms/`
| File | Function | Description |
|------|----------|-------------|
| `insertion_sort.py` | `insertion_sort(lst)` | Returns `(sorted_list, comparisons, swaps)` |
| `selection_sort.py` | `selection_sort(lst)` | Returns `(sorted_list, comparisons, swaps)` |
| `merge_sort.py` | `merge_sort(lst)` | Returns `(sorted_list, comparisons)` — stable, top-down recursive |
| `quicksort.py` | `quicksort(lst, pivot_strategy)` | Returns `(sorted_list, comparisons)` — supports `"last"` and `"median_of_three"` pivot strategies |

### `experiments/`
| File | Function | Description |
|------|----------|-------------|
| `input_generator.py` | `random_array(n)` | Uniform random permutation of 1…n |
| | `nearly_sorted_array(n, swap_pct=0.05)` | Sorted array with ~5% random swaps |
| | `reverse_sorted_array(n)` | n…1 |
| | `duplicates_heavy_array(n)` | n integers drawn from [1, n//10] |
| `runner.py` | `run_benchmarks()` | Runs all algorithm×distribution×n combos (5 trials each), writes CSV to `experiments/results/` |

### `analysis/`
| File | Function | Description |
|------|----------|-------------|
| `plot_results.py` | `plot_random_array_performance()` | Runtime chart for random distribution |
| | `plot_nearly_sorted_array_performance()` | Runtime chart for nearly sorted distribution |
| | `plot_reverse_sorted_array_performance()` | Runtime chart for reverse sorted distribution |
| | `plot_duplicates_heavy_array_performance()` | Runtime chart for duplicate-heavy distribution |
| | `show_summary_chart_max_n()` | Bar chart comparing all algorithms at their maximum n |

### `tests/`
| File | Description |
|------|-------------|
| `test_sorts.py` | Correctness tests for all four algorithms via `pytest` |
