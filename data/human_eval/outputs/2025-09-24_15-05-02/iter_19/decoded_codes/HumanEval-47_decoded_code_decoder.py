from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_list = sorted(list_of_elements)
    n = len(sorted_list)
    if n % 2 == 1:
        return float(sorted_list[n // 2])
    else:
        midpoint = n // 2
        return (sorted_list[midpoint - 1] + sorted_list[midpoint]) / 2