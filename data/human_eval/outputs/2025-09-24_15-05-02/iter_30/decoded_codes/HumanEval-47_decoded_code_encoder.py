from typing import List, Union

def median(list_l: List[Union[int, float]]) -> float:
    if not list_l:
        raise ValueError("median() arg is an empty list")
    sorted_l = sorted(list_l)
    n = len(sorted_l)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_l[mid])
    else:
        return (sorted_l[mid - 1] + sorted_l[mid]) / 2.0