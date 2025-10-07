from typing import List

def minPath(grid: List[List[int]], w: int) -> List[int]:
    q: int = len(grid)
    r: int = q * q + 1

    for u in range(q):
        for v in range(q):
            if grid[u][v] == 1:
                s: List[int] = []
                if u != 0:
                    s.append(grid[u - 1][v])
                if v != 0:
                    s.append(grid[u][v - 1])
                if u != q - 1:
                    s.append(grid[u + 1][v])
                if v != q - 1:
                    s.append(grid[u][v + 1])
                if s:
                    r = min(s)

    t: List[int] = []
    for x in range(w):
        t.append(1 if x % 2 == 0 else r)

    return t