from typing import Callable


def digitSum(zeta: str) -> int:
    def helper(theta: int, xi: int) -> int:
        if xi == len(zeta):
            return theta
        kappa = 0
        if 'A' <= zeta[xi] <= 'Z':
            kappa = ord(zeta[xi])
        return helper(theta + kappa, xi + 1)
    return helper(0, 1)