from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    ordered_copy = list_of_elements.copy()
    ordered_copy.sort()
    count = len(ordered_copy)
    midpoint = count // 2
    if count % 2 != 0:
        return float(ordered_copy[midpoint])
    left_val = ordered_copy[midpoint - 1]
    right_val = ordered_copy[midpoint]
    return (left_val + right_val) / 2.0