from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_elements = list_of_elements.copy()
    sorted_elements.sort()
    total_items = len(sorted_elements)
    if total_items % 2 != 0:
        middle_position = total_items // 2
        return float(sorted_elements[middle_position])
    lower_middle = (total_items // 2) - 1
    upper_middle = total_items // 2
    return (sorted_elements[lower_middle] + sorted_elements[upper_middle]) / 2.0