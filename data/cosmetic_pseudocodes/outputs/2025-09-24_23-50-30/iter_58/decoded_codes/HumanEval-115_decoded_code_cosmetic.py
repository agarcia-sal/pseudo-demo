from math import ceil
from typing import List

def max_fill(grid: List[List[int]], alpha: int) -> int:
    def beta(gamma: List[int]) -> int:
        delta = 0
        for zeta in gamma:
            delta += zeta
        return delta

    eta: List[int] = []
    iota = 0
    while iota < len(grid):
        kappa = beta(grid[iota])
        lamda = ceil(kappa / alpha)
        eta.append(lamda)
        iota += 1

    mu = 0
    for nu in eta:
        mu += nu
    return mu