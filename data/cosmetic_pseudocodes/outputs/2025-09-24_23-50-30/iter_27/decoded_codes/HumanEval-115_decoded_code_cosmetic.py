import math
from typing import List

def max_fill(grid: List[List[int]], volume: int) -> int:
    delta: List[int] = []
    idx: int = 0
    while idx < len(grid):
        omega: int = 0
        zeta: int = 0
        while zeta < len(grid[idx]):
            omega += grid[idx][zeta]
            zeta += 1
        delta.append(math.ceil(omega / volume))
        idx += 1
    kappa: int = 0
    lam: int = 0
    while lam < len(delta):
        kappa += delta[lam]
        lam += 1
    return kappa