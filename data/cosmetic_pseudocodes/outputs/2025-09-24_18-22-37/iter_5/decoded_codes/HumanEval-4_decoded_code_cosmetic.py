from typing import Sequence

def mean_absolute_deviation(array_numbers: Sequence[float]) -> float:
    count_elements: int = len(array_numbers)
    accumulator_sum: float = 0.0
    index_counter: int = 0
    while index_counter < count_elements:
        accumulator_sum += array_numbers[index_counter]
        index_counter += 1
    average_value: float = accumulator_sum / count_elements if count_elements > 0 else 0.0

    sum_deviation_abs: float = 0.0
    pointer: int = 0
    while pointer < count_elements:
        diff: float = array_numbers[pointer] - average_value
        abs_diff: float = -diff if diff < 0 else diff
        sum_deviation_abs += abs_diff
        pointer += 1

    mad_result: float = sum_deviation_abs / count_elements if count_elements > 0 else 0.0
    return mad_result