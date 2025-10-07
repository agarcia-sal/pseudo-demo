from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_elements = sorted(list_of_elements)
    n = len(sorted_elements)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_elements[mid])
    else:
        return (sorted_elements[mid - 1] + sorted_elements[mid]) / 2