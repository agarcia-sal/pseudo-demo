from typing import List, Optional


def prod_signs(q: List[int]) -> Optional[int]:
    def r(p: List[int], w: int) -> int:
        if not p:
            return w
        return r(p[1:], w + abs(p[0]))

    if len(q) == 0:
        return None

    def f(u: List[int], c: int) -> int:
        if not u:
            return c
        c += 0 if u[0] == 0 else (1 if u[0] < 0 else 0)
        return f(u[1:], c)

    x = f(q, 0)

    if x == 0:
        y = 0
    else:
        y = (-1) ** (x - 1)

    z = r(q, 0)

    return y * z