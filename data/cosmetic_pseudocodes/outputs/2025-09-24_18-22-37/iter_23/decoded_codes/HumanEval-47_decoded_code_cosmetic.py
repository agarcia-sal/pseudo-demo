from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_copy = sorted(list_of_elements)
    total_count = len(sorted_copy)
    remainder = total_count % 2
    if remainder != 1:
        mid_index = total_count // 2
        left_value = sorted_copy[mid_index - 1]
        right_value = sorted_copy[mid_index]
        return (left_value + right_value) / 2.0
    else:
        center = total_count // 2
        return float(sorted_copy[center])