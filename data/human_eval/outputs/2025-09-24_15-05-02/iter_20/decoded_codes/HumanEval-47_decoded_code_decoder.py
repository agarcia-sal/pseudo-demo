from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_list = sorted(list_of_elements)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_list[mid])
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2.0