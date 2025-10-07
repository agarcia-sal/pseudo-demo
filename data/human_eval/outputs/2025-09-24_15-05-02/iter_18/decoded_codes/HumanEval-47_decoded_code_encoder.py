from typing import List, Union

def median(l: List[Union[int, float]]) -> float:
    sorted_l = sorted(l)
    n = len(sorted_l)
    if n == 0:
        raise ValueError("median() arg is an empty list")
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_l[mid])
    else:
        return (sorted_l[mid - 1] + sorted_l[mid]) / 2.0