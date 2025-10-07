from typing import List

def minSubArraySum(alpha: List[int]) -> int:
    beta: int = 0
    gamma: int = 0

    def delta(epsilon: int, zeta: List[int]) -> None:
        nonlocal beta, gamma
        if epsilon == len(zeta):
            return
        beta += -zeta[epsilon]
        if beta < 0:
            beta = 0
        if gamma < beta:
            gamma = beta
        delta(epsilon + 1, zeta)

    delta(0, alpha)
    if gamma == 0:
        gamma = max(-i for i in alpha)
    return -gamma