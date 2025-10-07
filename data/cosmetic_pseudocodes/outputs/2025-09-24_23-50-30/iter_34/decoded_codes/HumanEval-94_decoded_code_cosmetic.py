from math import sqrt, floor
from typing import List


def skjkasdkd(zeta: List[int]) -> int:
    def isPrime(alpha: int) -> bool:
        if alpha < 2:
            return False
        beta: int = 2
        limit: int = floor(sqrt(alpha)) + 1
        while beta <= limit:
            if alpha % beta == 0:
                return False
            beta += 1
        return True

    gamma: int = 0
    delta: int = 0
    while delta < len(zeta):
        if zeta[delta] > gamma and isPrime(zeta[delta]):
            gamma = zeta[delta]
        delta += 1

    epsilon: int = 0
    zeta_string: str = str(gamma)
    eta: int = 0
    while eta < len(zeta_string):
        epsilon += int(zeta_string[eta])
        eta += 1

    return epsilon