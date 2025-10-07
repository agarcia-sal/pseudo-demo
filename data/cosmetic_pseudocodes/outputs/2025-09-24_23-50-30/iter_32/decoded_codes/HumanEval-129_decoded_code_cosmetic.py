from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    q: int = len(grid)
    u: int = (q * q) + 1

    for m in range(q):
        for r in range(q):
            if grid[m][r] == 1:
                w: List[int] = []
                if m != 0:
                    w.append(grid[m - 1][r])
                if r != 0:
                    w.append(grid[m][r - 1])
                if m != q - 1:
                    w.append(grid[m + 1][r])
                if r != q - 1:
                    w.append(grid[m][r + 1])
                if w:
                    u = min(w)

    p: List[int] = []
    for s in range(k):
        if s % 2 == 0:
            p.append(1)
        else:
            p.append(u)

    return p