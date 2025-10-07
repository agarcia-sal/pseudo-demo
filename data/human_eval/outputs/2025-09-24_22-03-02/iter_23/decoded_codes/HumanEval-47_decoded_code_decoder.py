from typing import List, Union

def median(l: List[Union[int, float]]) -> float:
    l = sorted(l)
    length = len(l)
    remainder = length % 2
    if remainder == 1:
        middle_index = length // 2
        return float(l[middle_index])
    else:
        middle_index1 = (length // 2) - 1
        middle_index2 = length // 2
        sum_ = l[middle_index1] + l[middle_index2]
        average = sum_ / 2.0
        return average