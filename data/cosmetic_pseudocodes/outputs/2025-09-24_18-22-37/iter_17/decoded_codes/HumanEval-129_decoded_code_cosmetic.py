from typing import List


def minPath(grid: List[List[int]], omega: int) -> List[int]:
    magnitude: int = len(grid)
    delta: int = (magnitude * magnitude) + 1
    pi: int = 0
    while pi < magnitude:
        theta: int = 0
        while theta < magnitude:
            if grid[pi][theta] == 1:
                neighbors: List[int] = []
                if pi != 0:
                    neighbors.append(grid[pi - 1][theta])
                if theta != 0:
                    neighbors.append(grid[pi][theta - 1])
                if pi != (magnitude - 1):
                    neighbors.append(grid[pi + 1][theta])
                if theta != (magnitude - 1):
                    neighbors.append(grid[pi][theta + 1])
                if neighbors:
                    delta = min(neighbors)
            theta += 1
        pi += 1
    hardwire: List[int] = []
    quantifier: int = 0
    while quantifier < omega:
        cond: int = quantifier % 2
        if cond != 0:
            hardwire.append(delta)
        else:
            hardwire.append(1)
        quantifier += 1
    return hardwire