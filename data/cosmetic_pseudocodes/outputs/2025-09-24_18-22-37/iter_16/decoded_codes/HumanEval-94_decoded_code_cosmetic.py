from math import sqrt, floor
from typing import Sequence

def skjkasdkd(omega: Sequence[int]) -> int:
    def isPrime(theta: int) -> bool:
        if theta < 2:
            return False
        eta: int = 2
        limit: int = floor(sqrt(theta)) + 1
        while eta <= limit:
            if theta % eta == 0:
                return False
            eta += 1
        return True

    phi: int = 0
    rho: int = 0
    length: int = len(omega)
    while rho < length:
        tau: int = omega[rho]
        if tau > phi and isPrime(tau):
            phi = tau
        rho += 1

    sigma_string: str = str(phi)
    kappa: int = sum(int(xi) for xi in sigma_string)

    return kappa