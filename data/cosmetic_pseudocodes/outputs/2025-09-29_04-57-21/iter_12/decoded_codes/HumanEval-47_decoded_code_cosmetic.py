from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_elements = sorted(list_of_elements)
    total_count = len(sorted_elements)

    if total_count % 2 != 0:
        center_index = total_count // 2
        return float(sorted_elements[center_index])

    mid1 = sorted_elements[(total_count // 2) - 1]
    mid2 = sorted_elements[total_count // 2]
    average = (mid1 + mid2) / 2.0
    return average