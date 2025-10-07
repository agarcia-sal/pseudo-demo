from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    z: int = len(grid)
    w: int = (z * z) + 1
    p: int = 0
    while p < z:
        q: int = 0
        while q < z:
            if grid[p][q] == 1:
                m: List[int] = []
                if p != 0:
                    m.append(grid[p - 1][q])
                if q != 0:
                    m.append(grid[p][q - 1])
                if p != z - 1:
                    m.append(grid[p + 1][q])
                if q != z - 1:
                    m.append(grid[p][q + 1])
                if m:
                    w = min(m)
            q += 1
        p += 1

    r: List[int] = []
    s: int = 0
    while s < k:
        if s % 2 == 0:
            r.append(1)
        else:
            r.append(w)
        s += 1

    return r