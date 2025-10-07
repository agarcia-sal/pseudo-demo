from typing import List, Union

def median(l: List[Union[int, float]]) -> float:
    l = sorted(l)
    n = len(l)
    mid = n // 2
    if n % 2 == 1:
        return float(l[mid])
    else:
        return (l[mid - 1] + l[mid]) / 2