from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_list = sorted(list_of_elements)
    length = len(sorted_list)
    mid = length // 2
    if length % 2 == 1:
        return float(sorted_list[mid])
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2.0