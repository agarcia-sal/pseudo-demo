from typing import Sequence

def minSubArraySum(alpha: Sequence[int]) -> int:
    omega: int = 0
    epsilon: int = 0
    zeta: int = 0
    eta: int = 0
    theta: int = 0
    i: int = 0  # zero-based indexing in Python
    n: int = len(alpha)
    while i < n:
        zeta = -alpha[i]
        epsilon += zeta
        if epsilon < 0:
            epsilon = 0
        if epsilon > omega:
            omega = epsilon
        i += 1
    if omega == 0:
        eta = -alpha[0]
        j: int = 0
        while j < n:
            theta = -alpha[j]
            if theta > eta:
                eta = theta
            j += 1
        omega = eta
    return -omega