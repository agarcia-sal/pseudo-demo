from typing import List, Union

def median(l: List[Union[int, float]]) -> float:
    l = sorted(l)
    length = len(l)
    remainder = length % 2
    if remainder == 1:
        middle_index = length // 2
        return float(l[middle_index])
    else:
        middle_right_index = length // 2
        middle_left_index = middle_right_index - 1
        middle_sum = l[middle_left_index] + l[middle_right_index]
        return middle_sum / 2.0