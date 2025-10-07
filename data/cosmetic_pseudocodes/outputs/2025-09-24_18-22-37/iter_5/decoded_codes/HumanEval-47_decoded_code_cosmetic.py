from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_elements = sorted(list_of_elements)
    total_count = len(sorted_elements)
    mid_index = total_count // 2

    if total_count % 2 != 0:
        return float(sorted_elements[mid_index])
    else:
        left_value = sorted_elements[mid_index - 1]
        right_value = sorted_elements[mid_index]
        return (left_value + right_value) / 2.0