from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    n: int = len(list_of_numbers)
    if n == 0:
        raise ValueError("list_of_numbers must not be empty")
    mean_value: float = 0.0
    for i in range(n):
        mean_value += list_of_numbers[i]
    mean_value /= n

    i: int = 0
    total_abs_diff: float = 0.0
    while i < n:
        if not (list_of_numbers[i] >= mean_value):
            diff: float = mean_value - list_of_numbers[i]
        else:
            diff = list_of_numbers[i] - mean_value
        total_abs_diff += diff
        i += 1

    return total_abs_diff / n