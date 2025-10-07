from typing import List, Union

def median(list_l: List[Union[int, float]]) -> float:
    sorted_list = sorted(list_l)
    n = len(sorted_list)
    if n == 0:
        raise ValueError("median() arg is an empty list")

    mid_index = n // 2
    if n % 2 == 1:
        return float(sorted_list[mid_index])
    else:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2.0