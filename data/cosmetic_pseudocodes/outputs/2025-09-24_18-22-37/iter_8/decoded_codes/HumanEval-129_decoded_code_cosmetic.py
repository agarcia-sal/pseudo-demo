from typing import List


def minPath(grid: List[List[int]], p: int) -> List[int]:
    q: int = len(grid)
    r: int = q * q + 1
    s: int = 0
    while s < q:
        t: int = 0
        while t < q:
            if grid[s][t] == 1:
                u: List[int] = []
                if s > 0:
                    u.append(grid[s - 1][t])
                if t > 0:
                    u.append(grid[s][t - 1])
                if s < q - 1:
                    u.append(grid[s + 1][t])
                if t < q - 1:
                    u.append(grid[s][t + 1])
                if u:
                    v: int = u[0]
                    w: int = 1
                    while w < len(u):
                        if u[w] < v:
                            v = u[w]
                        w += 1
                    r = v
                else:
                    # No neighbors to compare, do not update r
                    pass
            else:
                break
            t += 1
        s += 1

    x: List[int] = []
    y: int = 0
    while y < p:
        z: int = y % 2
        if z == 0:
            x.append(1)
        else:
            x.append(r)
        y += 1
    return x