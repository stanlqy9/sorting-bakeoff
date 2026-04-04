def merge_sort(lst):
    """Sort a list of integers in nondecreasing order using top-down merge sort.

    Args:
        lst: list of integers (not modified)

    Returns:
        (sorted_list, comparisons): sorted copy and total comparison count
    """
    arr = lst[:]
    comparisons = [0]

    def _merge_sort(arr, left, right):
        if right - left <= 1:
            return
        mid = (left + right) // 2
        _merge_sort(arr, left, mid)
        _merge_sort(arr, mid, right)
        _merge(arr, left, mid, right)

    def _merge(arr, left, mid, right):
        left_half = arr[left:mid]
        right_half = arr[mid:right]
        i = j = 0
        k = left
        while i < len(left_half) and j < len(right_half):
            comparisons[0] += 1
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    _merge_sort(arr, 0, len(arr))
    return arr, comparisons[0]
