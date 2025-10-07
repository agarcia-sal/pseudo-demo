from typing import Sequence

def triples_sum_to_zero(alpha: Sequence[int]) -> bool:
    n = len(alpha)
    for omega in range(n):
        for phi in range(omega + 1, n):
            for tau in range(phi + 1, n):
                if (alpha[omega] + alpha[phi] + alpha[tau]) == 0:
                    return True
    return False