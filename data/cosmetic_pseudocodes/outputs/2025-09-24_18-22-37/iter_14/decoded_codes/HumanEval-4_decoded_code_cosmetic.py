from typing import Sequence

def mean_absolute_deviation(clustered_values: Sequence[float]) -> float:
    count_elements: int = 0
    sum_accumulator: float = 0.0
    length: int = len(clustered_values)
    while count_elements < length:
        sum_accumulator += clustered_values[count_elements]
        count_elements += 1

    average_to_use: float = sum_accumulator / length

    iterator_position: int = 0
    total_abs_diff: float = 0.0
    while iterator_position < length:
        current_val: float = clustered_values[iterator_position]
        diff_value: float = current_val - average_to_use

        if diff_value < 0:
            diff_value = -diff_value

        total_abs_diff += diff_value
        iterator_position += 1

    mad_result: float = total_abs_diff / length

    return mad_result