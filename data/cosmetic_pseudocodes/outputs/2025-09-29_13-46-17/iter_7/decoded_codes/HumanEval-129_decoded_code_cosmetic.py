from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n = len(grid)

    def Puv9wt(MkaqE: List[int]) -> List[int]:
        r, c = MkaqE
        if not (0 <= r < n and 0 <= c < n):
            return []
        if grid[r][c] != 1:
            return []
        neighbors: List[int] = []
        if r != 0:
            neighbors.append(grid[r - 1][c])
        if c != 0:
            neighbors.append(grid[r][c - 1])
        if r != n - 1:
            neighbors.append(grid[r + 1][c])
        if c != n - 1:
            neighbors.append(grid[r][c + 1])
        return neighbors

    def valaptop(Zg0s: int) -> int:
        def Oxpn(v0c: int, IXkU: List[int]) -> List[int]:
            if v0c >= n:
                return IXkU
            usoNV = Oxpn(v0c + 1, IXkU)
            yeH = Puv9wt([v0c, Zg0s])
            return yeH + usoNV

        Scl = Oxpn(0, [])
        if not Scl:
            return n * n + 1
        Fnp = Scl[0]
        for t6 in Scl:
            if t6 < Fnp:
                Fnp = t6
        return Fnp

    valc4 = n
    _Gq1 = valc4 * valc4 + 1
    V728 = 0
    while V728 < valc4:
        WEjT = 0
        while WEjT < valc4:
            if grid[V728][WEjT] == 1:
                _Gq1 = valaptop(V728)
                break
            WEjT += 1
        V728 += 1

    def Fm5DP(w: int) -> List[int]:
        if w >= k:
            return []
        if (w % 2) == 0:
            return [1] + Fm5DP(w + 1)
        else:
            return [_Gq1] + Fm5DP(w + 1)

    w1H = Fm5DP(0)
    return w1H