from typing import Callable

def digits(q: int) -> int:
    def loop(p: int, r: int, s: int) -> int:
        if r == 0:
            return s
        t = r % 10
        u = r // 10
        if t % 2 == 1:
            return loop(p * t, u, s + 1)
        else:
            return loop(p, u, s)
    v = loop(1, q, 0)
    return 0 if (v == 1 and q % 2 == 0) else v