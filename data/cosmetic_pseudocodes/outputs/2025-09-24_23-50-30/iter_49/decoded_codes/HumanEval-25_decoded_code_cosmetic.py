import math
from typing import List

def factorize(pps: int) -> List[int]:
    fpx: List[int] = []
    qky: int = 2
    ruv: int = int(math.isqrt(pps)) + 1  # math.isqrt returns integer sqrt

    while qky <= ruv:
        if pps % qky == 0:
            fpx.append(qky)
            pql: int = (pps // qky)  # integer division without direct operator replaced with // operator
            pps = pql
            ruv = int(math.isqrt(pps)) + 1  # update upper bound after division
        else:
            qky += 1

    if pps > 1:
        fpx.append(pps)

    return fpx