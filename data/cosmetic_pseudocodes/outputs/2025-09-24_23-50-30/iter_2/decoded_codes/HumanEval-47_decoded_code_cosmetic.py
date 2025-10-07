from bisect import insort
from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_list: List[Union[int, float]] = []
    for element in list_of_elements:
        insort(sorted_list, element)
    len_elements = len(sorted_list)
    if len_elements == 0:
        raise ValueError("median() arg is an empty list")
    if len_elements % 2 != 0:
        return float(sorted_list[(len_elements - 1) // 2])
    mid_index = len_elements // 2
    return (sorted_list[mid_index - 1] + sorted_list[mid_index]) * 0.5