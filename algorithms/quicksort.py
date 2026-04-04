def quicksort(lst, pivot_strategy="median_of_three"):
    """Sort a list of integers in nondecreasing order using quicksort.

    Partition scheme: Lomuto. Chosen for straightforward implementation and
    easy comparison counting — each partition call makes exactly (high - low)
    comparisons against the pivot.

    Pivot strategies:
        "last"            – last element; simple baseline, O(n^2) on sorted input
        "median_of_three" – median of first, middle, last elements; reduces
                            worst-case likelihood on sorted/nearly-sorted input

    Args:
        lst:            list of integers (not modified)
        pivot_strategy: "last" or "median_of_three" (default)

    Returns:
        (sorted_list, comparisons): sorted copy and total comparison count
    """
    arr = lst[:]
    comparisons = [0]

    def _median_of_three(arr, low, high):
        mid = (low + high) // 2
        # Sort low, mid, high positions by value, then return mid as pivot index
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
        # Place pivot at high - 1 so Lomuto uses it naturally
        arr[mid], arr[high] = arr[high], arr[mid]
        return high

    def _partition(arr, low, high):
        if pivot_strategy == "median_of_three" and high - low >= 2:
            pivot_idx = _median_of_three(arr, low, high)
        else:
            pivot_idx = high
        pivot = arr[pivot_idx]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quicksort(arr, low, high):
        if low < high:
            p = _partition(arr, low, high)
            _quicksort(arr, low, p - 1)
            _quicksort(arr, p + 1, high)

    if arr:
        _quicksort(arr, 0, len(arr) - 1)
    return arr, comparisons[0]
