from typing import Sequence

def mean_absolute_deviation(numbers_collection: Sequence[float]) -> float:
    count_elements: int = len(numbers_collection)
    if count_elements == 0:
        raise ValueError("numbers_collection must contain at least one element")

    cumulative_sum: float = 0.0
    current_index: int = 0

    while current_index < count_elements:
        current_element: float = numbers_collection[current_index]
        cumulative_sum += current_element
        current_index += 1

    central_value: float = cumulative_sum / count_elements
    deviation_sum: float = 0.0
    current_index = 0

    while current_index < count_elements:
        current_element = numbers_collection[current_index]
        absolute_difference = current_element - central_value
        if absolute_difference < 0:
            absolute_difference = -absolute_difference
        deviation_sum += absolute_difference
        current_index += 1

    mad_result: float = deviation_sum / count_elements
    return mad_result