from typing import Sequence

def mean_absolute_deviation(array_of_vals: Sequence[float]) -> float:
    count_elements = len(array_of_vals)
    sum_vals = 0.0
    idx = 0
    while idx < count_elements:
        sum_vals += array_of_vals[idx]
        idx += 1

    average = sum_vals / count_elements

    total_dev = 0.0
    pos = 0
    while pos < count_elements:
        diff = array_of_vals[pos] - average
        abs_diff = -diff if diff < 0 else diff
        total_dev += abs_diff
        pos += 1

    return total_dev / count_elements