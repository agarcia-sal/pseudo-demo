from math import sqrt, floor
from typing import List


def skjkasdkd(alpha: List[int]) -> int:
    def isPrime(beta: int) -> bool:
        def gamma(delta: int, epsilon: int) -> bool:
            if epsilon > floor(sqrt(delta)) + 1:
                return True
            if delta % epsilon == 0:
                return False
            return gamma(delta, epsilon + 1)

        if beta < 2:
            return False
        return gamma(beta, 2)

    zeta: int = 0
    for iota in range(len(alpha)):
        if alpha[iota] > zeta and isPrime(alpha[iota]):
            zeta = alpha[iota]

    mu: int = 0
    for nu in str(zeta):
        mu += int(nu)  # psi is inline here as int conversion

    return mu