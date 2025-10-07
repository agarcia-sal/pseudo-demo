from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_list = sorted(list_of_elements)
    length = len(sorted_list)
    if length % 2 == 1:
        return sorted_list[length // 2]
    else:
        middle_index = length // 2
        return (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2