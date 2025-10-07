from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    temp_list = sorted(list_of_elements)
    n = len(temp_list)
    mid_pos = n // 2

    if n % 2 != 0:
        return float(temp_list[mid_pos])

    left_val = temp_list[mid_pos - 1]
    right_val = temp_list[mid_pos]
    median_val = (left_val + right_val) / 2.0
    return median_val