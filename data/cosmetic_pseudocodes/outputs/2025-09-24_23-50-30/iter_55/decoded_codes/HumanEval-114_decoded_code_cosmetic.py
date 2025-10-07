from typing import Sequence

def minSubArraySum(alpha: Sequence[int]) -> int:
    delta: int = 0
    beta: int = 0
    for epsilon in alpha:
        beta += -epsilon
        beta = max(beta, 0)
        delta = max(delta, beta)
    if delta == 0:
        gamma: int = -alpha[0]
        for i in range(1, len(alpha)):
            if -alpha[i] > gamma:
                gamma = -alpha[i]
        delta = gamma
    return -delta