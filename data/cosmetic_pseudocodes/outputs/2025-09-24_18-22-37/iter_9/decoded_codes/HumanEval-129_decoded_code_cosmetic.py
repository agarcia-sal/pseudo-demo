from typing import List

def minPath(grid: List[List[int]], alpha: int) -> List[int]:
    beta: int = len(grid)
    gamma: int = beta * beta + 1

    for delta in range(beta):
        for epsilon in range(beta):
            if grid[delta][epsilon] == 1:
                zeta: List[int] = []
                if delta != 0:
                    zeta.append(grid[delta - 1][epsilon])
                if epsilon != 0:
                    zeta.append(grid[delta][epsilon - 1])
                if delta != beta - 1:
                    zeta.append(grid[delta + 1][epsilon])
                if epsilon != beta - 1:
                    zeta.append(grid[delta][epsilon + 1])
                if zeta:
                    gamma = zeta[0]
                    for eta in range(1, len(zeta)):
                        if gamma > zeta[eta]:
                            gamma = zeta[eta]

    theta: List[int] = []
    for iota in range(alpha):
        if iota % 2 == 0:
            theta.append(1)
        else:
            theta.append(gamma)

    return theta