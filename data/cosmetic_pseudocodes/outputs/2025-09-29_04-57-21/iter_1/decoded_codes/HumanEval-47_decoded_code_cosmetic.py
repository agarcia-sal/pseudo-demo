from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_elements = sorted(list_of_elements)
    n = len(sorted_elements)
    if n % 2 != 0:
        return float(sorted_elements[n // 2])
    mid1 = sorted_elements[(n // 2) - 1]
    mid2 = sorted_elements[n // 2]
    return (mid1 + mid2) / 2.0