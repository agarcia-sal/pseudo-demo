from typing import Sequence

def exchange(alpha: Sequence[int], beta: Sequence[int]) -> str:
    xA: int = 0
    yB: int = 0
    idx1: int = 0
    while idx1 < len(alpha):
        val1: int = alpha[idx1]
        if val1 % 2 == 1:
            xA += 1
        idx1 += 1

    idx2: int = 0
    while idx2 < len(beta):
        val2: int = beta[idx2]
        if val2 % 2 == 0:
            yB += 1
        idx2 += 1

    if not (yB < xA):
        return "YES"
    else:
        return "NO"