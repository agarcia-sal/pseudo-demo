from typing import List

def mean_absolute_deviation(array_of_values: List[float]) -> float:
    def compute_sum(values: List[float], index: int, acc: float) -> float:
        if index >= len(values):
            return acc
        return compute_sum(values, index + 1, acc + values[index])

    length_var = len(array_of_values)
    if length_var == 0:
        return 0.0  # handle empty list robustly

    total_sum = compute_sum(array_of_values, 0, 0.0)
    mean_val = total_sum / length_var

    def abs_diff_sum(values: List[float], index: int, accumulator: float) -> float:
        if index == length_var:
            return accumulator
        difference = values[index] - mean_val
        abs_difference = -difference if difference < 0 else difference
        return abs_diff_sum(values, index + 1, accumulator + abs_difference)

    sum_abs_diff = abs_diff_sum(array_of_values, 0, 0.0)
    return sum_abs_diff / length_var