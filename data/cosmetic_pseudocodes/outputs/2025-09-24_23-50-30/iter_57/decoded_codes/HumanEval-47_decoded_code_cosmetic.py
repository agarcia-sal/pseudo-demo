from typing import Sequence, Union, overload

Number = Union[int, float]

def median(arr: Sequence[Number]) -> float:
    ordered = sorted(arr)
    n = len(ordered)
    odd_check = (n % 2) != 0
    if odd_check:
        center = n // 2
        return float(ordered[center])
    else:
        upper_mid = n // 2
        lower_mid = upper_mid - 1
        sum_mids = ordered[lower_mid] + ordered[upper_mid]
        return sum_mids / 2.0