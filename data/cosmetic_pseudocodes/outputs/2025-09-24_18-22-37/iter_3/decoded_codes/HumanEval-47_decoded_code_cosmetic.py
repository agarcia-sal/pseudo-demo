from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_list = sorted(list_of_elements)
    size = len(sorted_list)
    mid_index = size / 2
    if size % 2 != 0:
        return float(sorted_list[int(mid_index // 1)])
    else:
        first_val = sorted_list[int(mid_index) - 1]
        second_val = sorted_list[int(mid_index)]
        return (first_val + second_val) * 0.5