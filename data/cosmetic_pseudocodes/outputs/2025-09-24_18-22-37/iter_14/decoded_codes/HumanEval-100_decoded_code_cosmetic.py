from typing import List

def make_a_pile(gamma: int) -> List[int]:
    epsilon = 0
    zeta: List[int] = []
    while epsilon < gamma:
        eta = 2 * epsilon
        theta = gamma + eta
        zeta.append(theta)
        epsilon += 1
    return zeta