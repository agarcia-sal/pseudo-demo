from typing import List, Union

def median(l: List[Union[int, float]]) -> float:
    l = sorted(l)
    length = len(l)
    remainder = length % 2
    if remainder == 1:
        middle_index = length // 2
        return float(l[middle_index])
    else:
        middle_index = length // 2
        left_value = l[middle_index - 1]
        right_value = l[middle_index]
        sum_ = left_value + right_value
        average = sum_ / 2.0
        return average