from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    ordered_elements = list_of_elements.copy()
    ordered_elements.sort()

    total_items = len(ordered_elements)
    mid_position = total_items // 2

    if total_items % 2 == 0:
        return (ordered_elements[mid_position - 1] + ordered_elements[mid_position]) / 2.0

    return float(ordered_elements[mid_position])