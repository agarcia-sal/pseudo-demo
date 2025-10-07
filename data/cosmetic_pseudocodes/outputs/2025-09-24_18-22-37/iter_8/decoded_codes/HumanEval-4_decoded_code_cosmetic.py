from typing import Sequence

def mean_absolute_deviation(collection_of_values: Sequence[float]) -> float:
    count_of_elements: int = len(collection_of_values)
    if count_of_elements == 0:
        raise ValueError("collection_of_values must not be empty")
    accumulated_sum: float = 0.0
    current_index: int = 0
    while current_index < count_of_elements:
        accumulated_sum += collection_of_values[current_index]
        current_index += 1
    average_value: float = accumulated_sum / count_of_elements

    sum_of_absolute_differences: float = 0.0
    counter: int = 0
    while counter < count_of_elements:
        difference = collection_of_values[counter] - average_value
        if difference < 0:
            absolute_difference = -difference
        else:
            absolute_difference = difference
        sum_of_absolute_differences += absolute_difference
        counter += 1

    result_mad: float = sum_of_absolute_differences / count_of_elements
    return result_mad