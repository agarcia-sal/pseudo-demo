from typing import Sequence

def exchange(beta: Sequence[int], gamma: Sequence[int]) -> str:
    theta: int = 0
    alpha: int = 0
    i: int = 0
    while i < len(beta):
        delta: int = beta[i]
        if (delta - ((delta // 2) * 2)) == 1:  # check if delta is odd
            theta += 1
        i += 1

    j: int = 0
    while j < len(gamma):
        epsilon: int = gamma[j]
        if (epsilon - ((epsilon // 2) * 2)) == 0:  # check if epsilon is even
            alpha += 1
        j += 1

    if alpha >= theta:
        return "YES"
    else:
        return "NO"