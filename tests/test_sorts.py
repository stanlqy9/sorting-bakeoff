import random
import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort
from algorithms.merge_sort import merge_sort
from algorithms.quicksort import quicksort


#  Test data 

EMPTY = []
SINGLE = [42]
ALREADY_SORTED = [1, 2, 3, 4, 5, 6, 7, 8]
REVERSE_SORTED = [8, 7, 6, 5, 4, 3, 2, 1]
DUPLICATES = [4, 2, 4, 1, 3, 2, 4, 1, 3, 2]
LARGE_RANDOM = random.sample(range(1, 10_001), 10_000)


#  Helpers

def _check_quadratic_sort(sort_fn, input_list):
    """Validate a sort that returns (sorted_list, comparisons, swaps)."""
    original = list(input_list)          # snapshot before call
    sorted_list, comparisons, swaps = sort_fn(input_list)

    assert sorted_list == sorted(original)
    assert input_list == original        # must not modify the original
    assert comparisons >= 0
    assert swaps >= 0


def _check_nlogn_sort(sort_fn, input_list):
    """Validate a sort that returns (sorted_list, comparisons)."""
    original = list(input_list)
    sorted_list, comparisons = sort_fn(input_list)

    assert sorted_list == sorted(original)
    assert input_list == original
    assert comparisons >= 0


#  Insertion Sort

class TestInsertionSort:
    def test_empty(self):
        _check_quadratic_sort(insertion_sort, EMPTY)

    def test_single(self):
        _check_quadratic_sort(insertion_sort, SINGLE)

    def test_already_sorted(self):
        _check_quadratic_sort(insertion_sort, ALREADY_SORTED)

    def test_reverse_sorted(self):
        _check_quadratic_sort(insertion_sort, REVERSE_SORTED)

    def test_duplicates(self):
        _check_quadratic_sort(insertion_sort, DUPLICATES)

    def test_large_random(self):
        _check_quadratic_sort(insertion_sort, LARGE_RANDOM)


# Selection Sort 

class TestSelectionSort:
    def test_empty(self):
        _check_quadratic_sort(selection_sort, EMPTY)

    def test_single(self):
        _check_quadratic_sort(selection_sort, SINGLE)

    def test_already_sorted(self):
        _check_quadratic_sort(selection_sort, ALREADY_SORTED)

    def test_reverse_sorted(self):
        _check_quadratic_sort(selection_sort, REVERSE_SORTED)

    def test_duplicates(self):
        _check_quadratic_sort(selection_sort, DUPLICATES)

    def test_large_random(self):
        _check_quadratic_sort(selection_sort, LARGE_RANDOM)


# Merge Sort 

class TestMergeSort:
    def test_empty(self):
        _check_nlogn_sort(merge_sort, EMPTY)

    def test_single(self):
        _check_nlogn_sort(merge_sort, SINGLE)

    def test_already_sorted(self):
        _check_nlogn_sort(merge_sort, ALREADY_SORTED)

    def test_reverse_sorted(self):
        _check_nlogn_sort(merge_sort, REVERSE_SORTED)

    def test_duplicates(self):
        _check_nlogn_sort(merge_sort, DUPLICATES)

    def test_large_random(self):
        _check_nlogn_sort(merge_sort, LARGE_RANDOM)


#  Quicksort

class TestQuicksort:
    def test_empty(self):
        _check_nlogn_sort(quicksort, EMPTY)

    def test_single(self):
        _check_nlogn_sort(quicksort, SINGLE)

    def test_already_sorted(self):
        _check_nlogn_sort(quicksort, ALREADY_SORTED)

    def test_reverse_sorted(self):
        _check_nlogn_sort(quicksort, REVERSE_SORTED)

    def test_duplicates(self):
        _check_nlogn_sort(quicksort, DUPLICATES)

    def test_large_random(self):
        _check_nlogn_sort(quicksort, LARGE_RANDOM)
