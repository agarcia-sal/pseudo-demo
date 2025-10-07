from typing import List, Union

def median(list_l: List[Union[int, float]]) -> Union[int, float]:
    if not list_l:
        raise ValueError("median() arg is an empty list")
    sorted_list = sorted(list_l)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 1:
        return sorted_list[mid]
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2.0