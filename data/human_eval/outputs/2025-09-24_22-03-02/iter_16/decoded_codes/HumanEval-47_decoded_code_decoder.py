from typing import List, Union

def median(l: List[Union[int, float]]) -> float:
    l = sorted(l)
    n = len(l)
    if n % 2 == 1:
        return float(l[n // 2])
    else:
        return (l[(n // 2) - 1] + l[n // 2]) / 2.0