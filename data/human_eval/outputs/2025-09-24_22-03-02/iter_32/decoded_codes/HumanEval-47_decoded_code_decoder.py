from typing import List, Union

def median(l: List[Union[int, float]]) -> float:
    l = sorted(l)
    length = len(l)
    remainder = length % 2
    if remainder == 1:
        middle_index = length // 2
        result = l[middle_index]
        return float(result)
    else:
        middle_left_index = (length // 2) - 1
        middle_right_index = length // 2
        sum_of_middles = l[middle_left_index] + l[middle_right_index]
        result = sum_of_middles / 2.0
        return result