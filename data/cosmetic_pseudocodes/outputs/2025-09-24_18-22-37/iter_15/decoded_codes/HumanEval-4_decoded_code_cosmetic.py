from typing import Sequence


def mean_absolute_deviation(delta_values: Sequence[float]) -> float:
    delta_count: int = len(delta_values)
    if delta_count == 0:
        return 0.0  # Handle empty input gracefully

    accumulation: float = 0.0
    current_index: int = 0
    while current_index < delta_count:
        accumulation += delta_values[current_index]
        current_index += 1
    average_value: float = accumulation / delta_count

    sum_abs_diff: float = 0.0
    walker: int = 0
    while walker < delta_count:
        temporary_value: float = delta_values[walker] - average_value
        if temporary_value < 0:
            magnitude: float = -temporary_value
        else:
            magnitude = temporary_value
        sum_abs_diff += magnitude
        walker += 1

    result_variable: float = sum_abs_diff / delta_count
    return result_variable