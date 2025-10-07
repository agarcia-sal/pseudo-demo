from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_elements = list_of_elements.copy()
    sorted_elements.sort()

    size = len(sorted_elements)
    middle_index = size // 2
    remainder = size % 2

    if remainder == 1:
        return float(sorted_elements[middle_index])
    else:
        first_value = sorted_elements[middle_index - 1]
        second_value = sorted_elements[middle_index]
        average_value = (first_value + second_value) / 2.0
        return float(average_value)