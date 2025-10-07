from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    if not list_of_elements:
        raise ValueError("median() arg is an empty list")
    sorted_list: List[Union[int, float]] = sorted(list_of_elements)
    n: int = len(sorted_list)
    mid: int = n // 2
    if n % 2 == 1:
        return float(sorted_list[mid])
    else:
        middle_left = sorted_list[mid - 1]
        middle_right = sorted_list[mid]
        return (middle_left + middle_right) / 2.0