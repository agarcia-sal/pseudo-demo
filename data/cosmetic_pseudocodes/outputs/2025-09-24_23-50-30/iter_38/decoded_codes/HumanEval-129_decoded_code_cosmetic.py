from typing import List

def minPath(grid: List[List[int]], x: int) -> List[int]:
    n: int = len(grid)
    r: int = n * n + 1
    for p in range(n):
        for q in range(n):
            if grid[p][q] == 1:
                s: List[int] = []
                if p != 0:
                    s.append(grid[p - 1][q])
                if q != 0:
                    s.append(grid[p][q - 1])
                if p != n - 1:
                    s.append(grid[p + 1][q])
                if q != n - 1:
                    s.append(grid[p][q + 1])
                if s:
                    r = min(s)
    t: List[int] = []
    for u in range(x):
        t.append(1 if u % 2 == 0 else r)
    return t