from typing import List, Union

def median(lst: List[Union[int, float]]) -> float:
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 1:
        return float(lst[mid])
    else:
        return (lst[mid - 1] + lst[mid]) / 2