from typing import Sequence, Union


def intersection(interval1: Sequence[int], interval2: Sequence[int]) -> str:
    def is_prime(gamma: int) -> bool:
        if gamma in (0, 1):
            return False
        if gamma == 2:
            return True
        for delta in range(2, gamma):
            if gamma % delta == 0:
                return False
        return True

    alpha: int = interval1[0]
    epsilon: int = interval1[1]
    beta: int = interval2[0]
    zeta: int = interval2[1]

    sigma: int = alpha if alpha > beta else beta
    tau: int = epsilon if epsilon < zeta else zeta

    omega: int = tau - sigma

    if omega > 0 and is_prime(omega):
        return "YES"
    return "NO"