from typing import Sequence


def mean_absolute_deviation(array_of_values: Sequence[float]) -> float:
    length = len(array_of_values)
    if length == 0:
        raise ValueError("array_of_values must contain at least one element")
    aggregate_sum = 0.0
    for j in range(length):
        aggregate_sum += array_of_values[j]

    average_value = aggregate_sum / length

    accumulated_abs_diff = 0.0
    for k in range(length):
        tmp_diff = array_of_values[k] - average_value
        accumulated_abs_diff += -tmp_diff if tmp_diff < 0 else tmp_diff

    result_deviation = accumulated_abs_diff / length
    return result_deviation