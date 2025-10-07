from typing import List, Union

def median(list_l: List[Union[int, float]]) -> Union[int, float, None]:
    if not list_l:
        return None  # Handle empty list edge case by returning None
    sorted_list = sorted(list_l)
    n = len(sorted_list)
    mid_index = n // 2
    if n % 2 == 1:
        return sorted_list[mid_index]
    return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2.0