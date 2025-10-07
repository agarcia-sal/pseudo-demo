from typing import List, Union, Sequence

def median(list_of_elements: Sequence[Union[int, float]]) -> float:
    sorted_elements: List[Union[int, float]] = sorted(list_of_elements)
    total_elements: int = len(sorted_elements)
    midpoint: int = total_elements // 2

    if total_elements % 2 != 0:
        return float(sorted_elements[midpoint])

    left_of_center = sorted_elements[midpoint - 1]
    right_of_center = sorted_elements[midpoint]
    return (left_of_center + right_of_center) * 0.5