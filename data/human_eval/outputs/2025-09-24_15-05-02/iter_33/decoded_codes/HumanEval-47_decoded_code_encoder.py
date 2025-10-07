from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_list: List[Union[int, float]] = sorted(list_of_elements)
    n: int = len(sorted_list)
    mid: int = n // 2
    if n % 2 == 1:
        return float(sorted_list[mid])  # odd length: middle element
    else:
        # even length: average of two middle elements
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2.0