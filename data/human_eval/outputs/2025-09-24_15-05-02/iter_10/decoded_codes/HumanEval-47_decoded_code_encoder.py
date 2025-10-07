from typing import List, Union

def median(list_l: List[Union[int, float]]) -> float:
    sorted_list = sorted(list_l)
    length = len(sorted_list)
    if length % 2 == 1:
        return float(sorted_list[length // 2])
    middle_index = length // 2
    return (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2.0