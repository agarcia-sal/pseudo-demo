from math import sqrt
from typing import List

def skjkasdkd(alpha: List[int]) -> int:
    def isPrime(beta: int) -> bool:
        if beta < 2:
            return False
        limit = int(sqrt(beta)) + 1
        for gamma in range(2, limit):
            if beta % gamma == 0:
                return False
        return True

    delta = 0
    epsilon = 0
    while epsilon < len(alpha):
        if not (alpha[epsilon] <= delta) and isPrime(alpha[epsilon]):
            delta = alpha[epsilon]
        epsilon += 1

    zeta = 0
    eta = 0
    delta_str = str(delta)
    while eta < len(delta_str):
        theta = delta_str[eta]
        zeta += int(theta)
        eta += 1

    return zeta