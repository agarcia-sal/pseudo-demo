from math import floor, sqrt
from typing import List


def factorize(integer_omega: int) -> List[int]:
    sequence_alpha: List[int] = []
    term_beta: int = 2
    while term_beta <= floor(sqrt(integer_omega)) + 1:
        if integer_omega % term_beta == 0:
            sequence_alpha.append(term_beta)
            integer_omega //= term_beta
        else:
            term_beta += 1
    if integer_omega > 1:
        sequence_alpha.append(integer_omega)
    return sequence_alpha