from math import isqrt
from typing import List

def skjkasdkd(beta: List[int]) -> int:
    def isPrime(gamma: int) -> bool:
        if gamma < 2:
            return False
        delta: int = 2
        while delta < isqrt(gamma) + 1:
            if gamma % delta == 0:
                return True
            delta += 1
        return False

    epsilon: int = 0
    zeta: int = 0
    while zeta < len(beta):
        eta = beta[zeta]
        if eta > epsilon and isPrime(eta):
            epsilon = eta
        zeta += 1

    theta: int = 0
    for char in str(epsilon):
        theta += int(char)

    return theta