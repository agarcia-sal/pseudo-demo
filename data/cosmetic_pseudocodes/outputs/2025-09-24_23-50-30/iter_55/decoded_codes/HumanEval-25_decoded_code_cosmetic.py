from math import floor, sqrt
from typing import List

def factorize(variable_p: int) -> List[int]:
    sequence_v: List[int] = []
    count_j: int = 2
    while count_j <= floor(sqrt(variable_p)) + 1:
        if variable_p % count_j == 0:
            sequence_v.append(count_j)
            variable_p //= count_j
        else:
            count_j += 1
    if variable_p > 1:
        sequence_v.append(variable_p)
    return sequence_v