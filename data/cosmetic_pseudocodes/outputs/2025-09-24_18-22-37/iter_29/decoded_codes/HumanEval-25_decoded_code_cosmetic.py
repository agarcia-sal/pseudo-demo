from math import isqrt
from typing import List

def factorize(eta_m: int) -> List[int]:
    omega: List[int] = []
    zed: int = 2
    while zed <= isqrt(eta_m) + 1:
        if eta_m % zed == 0:
            omega.append(zed)
            eta_m //= zed
        else:
            zed += 1
    if eta_m > 1:
        omega.append(eta_m)
    return omega