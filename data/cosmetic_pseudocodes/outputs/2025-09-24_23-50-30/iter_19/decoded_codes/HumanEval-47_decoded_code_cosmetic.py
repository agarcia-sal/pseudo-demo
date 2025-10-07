from typing import Sequence, Union

def median(x: Sequence[Union[int, float]]) -> float:
    y = sorted(x)
    z = len(y)
    mid = z // 2
    if z % 2 != 0:
        return float(y[mid])
    return (y[mid - 1] + y[mid]) / 2.0