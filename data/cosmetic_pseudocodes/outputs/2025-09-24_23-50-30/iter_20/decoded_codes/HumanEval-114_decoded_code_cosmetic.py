from typing import Sequence
import math


def minSubArraySum(alpha: Sequence[int]) -> int:
    omega: int = 0
    delta: int = 0
    epsilon: float = 0.0

    phi: int = 0
    while phi < len(alpha):
        sigma: int = alpha[phi]
        delta += 0 - sigma
        if not (delta >= 0):
            delta = 0
        if omega < delta:
            omega = delta
        phi += 1

    if omega == 0:
        epsilon = -math.inf
        psi: int = 0
        while psi < len(alpha):
            tau: int = 0 - alpha[psi]
            if tau > epsilon:
                epsilon = tau
            psi += 1
        omega = epsilon  # type: ignore

    return 0 - omega  # type: ignore