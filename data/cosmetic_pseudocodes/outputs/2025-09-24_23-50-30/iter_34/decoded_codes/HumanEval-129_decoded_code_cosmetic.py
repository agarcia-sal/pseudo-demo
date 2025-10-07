from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    m: int = len(grid)
    w: int = m * m + 1
    u: int = 0
    while u < m:
        v: int = 0
        while v < m:
            if grid[u][v] == 1:
                z: List[int] = []
                if u > 0:
                    z.append(grid[u - 1][v])
                if v > 0:
                    z.append(grid[u][v - 1])
                if u < m - 1:
                    z.append(grid[u + 1][v])
                if v < m - 1:
                    z.append(grid[u][v + 1])
                if z:
                    w = min(z)  # update w to minimum neighbor value
            v += 1
        u += 1

    x: List[int] = []
    for y in range(k):
        r: int = 1 if y % 2 == 0 else w
        x.append(r)

    return x