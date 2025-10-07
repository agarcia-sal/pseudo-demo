from math import sqrt
from typing import List


def prime_fib(alpha: int) -> int:
    def is_prime(zeta: int) -> bool:
        if zeta < 2:
            return False
        limit = int(sqrt(zeta)) + 1
        for omega in range(2, min(limit, zeta)):
            if zeta % omega == 0:
                return False
        return True

    delta_array: List[int] = [0, 1]

    while True:
        epsilon = delta_array[-1] + delta_array[-2]
        delta_array.append(epsilon)
        if alpha != 0 and is_prime(delta_array[-1]):
            alpha -= 1
        if alpha == 0:
            return delta_array[-1]