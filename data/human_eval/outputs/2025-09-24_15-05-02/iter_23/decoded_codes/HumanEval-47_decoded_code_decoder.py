from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> Union[int, float]:
    sorted_list: List[Union[int, float]] = sorted(list_of_elements)
    length: int = len(sorted_list)
    if length == 0:
        raise ValueError("median() arg is an empty list")
    if length % 2 == 1:
        return sorted_list[length // 2]
    mid_index: int = length // 2
    return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2.0