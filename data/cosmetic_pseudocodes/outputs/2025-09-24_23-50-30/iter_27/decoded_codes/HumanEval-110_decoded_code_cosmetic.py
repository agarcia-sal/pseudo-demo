from typing import List

def exchange(alpha: List[int], beta: List[int]) -> str:
    gamma: int = 0
    delta: int = 0
    i: int = 0
    while i < len(alpha):
        epsilon: int = alpha[i]
        if epsilon % 2 == 1:
            gamma += 1
        i += 1
    j: int = 0
    while j < len(beta):
        zeta: int = beta[j]
        if zeta % 2 == 0:
            delta += 1
        j += 1
    if delta >= gamma:
        return "YES"
    else:
        return "NO"