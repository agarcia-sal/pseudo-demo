from typing import Sequence, Union

def median(collection_of_values: Sequence[Union[int, float]]) -> float:
    sorted_values = sorted(collection_of_values)
    size_of_values = len(sorted_values)
    is_odd_length = (size_of_values % 2) == 1

    if not is_odd_length:
        midpoint = size_of_values // 2
        first_middle_element = sorted_values[midpoint - 1]
        second_middle_element = sorted_values[midpoint]
        sum_middle_elements = first_middle_element + second_middle_element
        median_value = sum_middle_elements / 2.0
        return median_value
    else:
        middle_index = size_of_values // 2
        median_value = sorted_values[middle_index]
        return float(median_value)