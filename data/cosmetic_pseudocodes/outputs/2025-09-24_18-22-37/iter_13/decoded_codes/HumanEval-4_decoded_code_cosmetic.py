from typing import Sequence


def mean_absolute_deviation(numbers_collection: Sequence[float]) -> float:
    total_elements: int = len(numbers_collection)
    if total_elements == 0:
        raise ValueError("numbers_collection must not be empty")
    accumulated_sum: float = 0.0
    iterator_index: int = 0
    while iterator_index < total_elements:
        accumulated_sum += numbers_collection[iterator_index]
        iterator_index += 1
    average_value: float = accumulated_sum / total_elements
    sum_of_deviations: float = 0.0
    walk_index: int = 0
    while True:
        current_element = numbers_collection[walk_index]
        deviation = current_element - average_value
        if deviation < 0:
            deviation = -deviation
        sum_of_deviations += deviation
        walk_index += 1
        if walk_index == total_elements:
            break
    mad_result: float = sum_of_deviations / total_elements
    return mad_result