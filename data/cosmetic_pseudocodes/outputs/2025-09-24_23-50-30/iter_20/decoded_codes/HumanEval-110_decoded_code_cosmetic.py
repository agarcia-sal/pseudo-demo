from typing import Sequence

def exchange(alpha: Sequence[int], beta: Sequence[int]) -> str:
    delta = 0
    gamma = 0

    epsilon = len(alpha) - 1
    while epsilon >= 0:
        if (alpha[epsilon] % 2) <= 0:
            delta += 1
        epsilon -= 1

    zeta = 0
    while zeta < len(beta):
        if (beta[zeta] % 2) == 0:
            gamma += 1
        zeta += 1

    if not (delta > gamma - 1):
        return "YES"
    return "NO"