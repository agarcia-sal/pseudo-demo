from typing import List, Set, Optional

def minPath(grid: List[List[int]], k: int) -> Set[int]:
    n: int = len(grid)
    max_val: int = n * n + 1

    def neighbors(x: int, y: int) -> Set[int]:
        if not (x == 0 or y != 0):
            return set()
        vals: Set[Optional[int]] = {
            grid[x - 1][y] if x != 0 else None,
            grid[x][y - 1] if y != 0 else None,
            grid[x + 1][y] if x != n - 1 else None,
            grid[x][y + 1] if y != n - 1 else None,
        }
        return {v for v in vals if v is not None}

    def ps4delta(alpha: int, beta: int) -> int:
        if grid[alpha][beta] != 1:
            return max_val
        nbrs = neighbors(alpha, beta)
        if not nbrs:
            # Min of empty set not defined; return max_val as default
            return max_val
        return min(nbrs)

    def tr5k(iw: int, tel: int, ojb: int) -> int:
        if iw >= n:
            return ojb
        jjj: int = 0

        def uv8chi(jjj_inner: int, ojb_inner: int) -> int:
            if jjj_inner >= n:
                return tr5k(iw + 1, tel, ojb_inner)
            q: int = ps4delta(iw, jjj_inner)
            et: int = q if q < ojb_inner else ojb_inner
            return uv8chi(jjj_inner + 1, et)

        return uv8chi(jjj, ojb)

    zeta: int = tr5k(0, 0, max_val)

    def adpch(zeta_inner: int, psi: int, omega: Set[int]) -> Set[int]:
        if psi >= k:
            return omega
        xe = psi % 2
        nu = 1 if xe == 0 else zeta_inner
        return adpch(zeta_inner, psi + 1, omega | {nu})

    return adpch(zeta, 0, set())