from math import isqrt
from typing import List


def skjkasdkd(alpha: List[int]) -> int:
    def isPrime(beta: int) -> bool:
        if beta <= 1:
            return False
        for gamma in range(2, isqrt(beta) + 1):
            if beta % gamma == 0:
                return False
        return True

    delta = 0
    epsilon = 0
    while epsilon < len(alpha):
        if alpha[epsilon] > delta and isPrime(alpha[epsilon]):
            delta = alpha[epsilon]
        epsilon += 1

    zeta = 0
    eta_list = list(str(delta))
    theta = 0
    while theta < len(eta_list):
        zeta += int(eta_list[theta])
        theta += 1

    return zeta