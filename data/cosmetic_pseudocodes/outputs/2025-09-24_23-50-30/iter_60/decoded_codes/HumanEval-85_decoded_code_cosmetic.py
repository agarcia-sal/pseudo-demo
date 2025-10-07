from typing import Sequence

def add(delta: Sequence[int]) -> int:
    def helper(zeta: Sequence[int], theta: int, iota: int) -> int:
        if iota > len(zeta):
            return theta
        elif (zeta[iota - 1] % 2) == 0:
            return helper(zeta, theta + zeta[iota - 1], iota + 2)
        else:
            return helper(zeta, theta, iota + 2)
    return helper(delta, 0, 1)