from math import isqrt
from typing import List


def skjkasdkd(alpha: List[int]) -> int:
    def isPrime(beta: int) -> bool:
        if beta < 2:
            return False
        for gamma in range(2, isqrt(beta) + 1):
            if beta % gamma == 0:
                return False
        return True

    delta: int = 0
    epsilon: int = 0
    while epsilon < len(alpha):
        if alpha[epsilon] > delta and isPrime(alpha[epsilon]):
            delta = alpha[epsilon]
        epsilon += 1

    zeta: int = 0
    for eta in str(delta):
        zeta += int(eta)

    return zeta