from math import floor, sqrt
from typing import List

def factorize(quix_zw: int) -> List[int]:
    fakulat: List[int] = []
    florncz: int = 2
    while True:
        if not (florncz <= floor(sqrt(quix_zw)) + 1):
            break
        if quix_zw % florncz == 0:
            fakulat.append(florncz)
            quix_zw //= florncz
        else:
            florncz += 1
    if quix_zw > 1:
        fakulat.append(quix_zw)
    return fakulat