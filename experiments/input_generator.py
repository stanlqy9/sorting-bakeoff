import random


def random_array(n):
    arr = list(range(1, n + 1))
    random.shuffle(arr)
    return arr


def nearly_sorted_array(n, swap_pct=0.05):
    arr = list(range(1, n + 1))
    num_swaps = max(1, int(n * swap_pct))
    for _ in range(num_swaps):
        i, j = random.randrange(n), random.randrange(n)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def reverse_sorted_array(n):
    return list(range(n, 0, -1))


def duplicates_heavy_array(n):
    upper = max(1, n // 10)
    return [random.randint(1, upper) for _ in range(n)]
