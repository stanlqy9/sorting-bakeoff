def quicksort(input_list, pivot_strategy="median_of_three"):
    """
    Sort a list in nondecreasing order using quicksort.

    Args:
        input_list: list of integers
        pivot_strategy: "last" or "median_of_three"

    Returns:
        (sorted_list, comparisons)
    """
    # Create a copy so we do NOT modify the orginal input list
    arr = input_list.copy()

    # Call the recursive helper to sort the array and count comparisons 
    comparisons = _quicksort_helper(arr, 0, len(arr) - 1, pivot_strategy)

    # Return the sorted array and total number of comparisons
    return arr, comparisons


def _quicksort_helper(arr, low, high, pivot_strategy):
    # Initialize comparison counter for this recursive call
    comparisons = 0

    # Only proceed if there are at least 2 elements to sort
    if low < high:
        # Partition the array and get pivot position + comparisons made
        pivot_index, part_comparisons = _partition(arr, low, high, pivot_strategy)

        # Add partition comparisons to total
        comparisons += part_comparisons

        # Recursively sort the left side of the pivot
        comparisons += _quicksort_helper(arr, low, pivot_index - 1, pivot_strategy)

        # Recurively sort the right side of the pivot
        comparisons += _quicksort_helper(arr, pivot_index + 1, high, pivot_strategy)

    # Return total comparisons from this call
    return comparisons


def _partition(arr, low, high, pivot_strategy):
    """
    Lomuto partition scheme.
    Returns:
        (pivot_final_index, comparisons)
    """
    # Choose pivot based on selected strategy
    if pivot_strategy == "median_of_three":

        # Get index of median at first, middle, last elements
        pivot_index = _median_of_three(arr, low, high)

        # Swap chosen pivot with last element 
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    elif pivot_strategy == "last":

        # Use last element directly as pivot
        pivot_index = high

    else:
        # Handle invalid pivot strategy input
        raise ValueError("pivot_strategy must be 'last' or 'median_of_three'")
    
    # Set pivot value (currently located at the end of array)
    pivot = arr[high]

    # i tracks the boundary of elements <= pivot
    i = low - 1

    # Initialize comparison counter
    comparisons = 0

    # Iterate through the subarray (exclluding the pivot)
    for j in range(low, high):

        # Count each comparison with pivot
        comparisons += 1

        # If current element should go to the left of pivot
        if arr[j] <= pivot:

            # Move boundary forward
            i += 1

            # Swap current element into correct position
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its final sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return pivot's final index and total comparisons
    return i + 1, comparisons


def _median_of_three(arr, low, high):
    """
    Return the index of the median value among:
    arr[low], arr[mid], arr[high]
    """

    # Compute middle index
    mid = (low + high) // 2

    #Get values of low, mid, and high positions
    a = arr[low]
    b = arr[mid]
    c = arr[high]

    # Check if middle value is the median
    if a <= b <= c or c <= b <= a:
        return mid
    
    # Check if first value is the median
    elif b <= a <= c or c <= a <= b:
        return low
    
    # Otherwise, last value is the median
    else:
        return high
    

