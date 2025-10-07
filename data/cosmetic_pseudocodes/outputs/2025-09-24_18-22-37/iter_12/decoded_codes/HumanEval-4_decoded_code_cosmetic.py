from typing import Sequence

def mean_absolute_deviation(array_input: Sequence[float]) -> float:
    count_elements: int = len(array_input)
    if count_elements == 0:
        raise ValueError("Input array must contain at least one element")
    sum_values: float = 0.0
    idx: int = 0
    while idx < count_elements:
        sum_values += array_input[idx]
        idx += 1
    average_value: float = sum_values / count_elements
    total_deviation: float = 0.0
    for idx in range(count_elements):
        current_diff: float = array_input[idx] - average_value
        abs_diff: float = current_diff if current_diff >= 0 else -current_diff
        total_deviation += abs_diff
    mad_result: float = total_deviation / count_elements
    return mad_result