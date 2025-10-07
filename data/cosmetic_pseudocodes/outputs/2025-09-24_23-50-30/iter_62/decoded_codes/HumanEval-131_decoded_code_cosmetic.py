from typing import Callable


def digits(q: int) -> int:
    def loop(p: int, r: str, s: int) -> int:
        if s == len(r):
            return 0 if p == 1 else p
        c = r[s]
        d = int(c)
        if d % 2 != 0:
            return loop(p * d, r, s + 1)
        else:
            return loop(p, r, s + 1)
    return loop(1, str(q), 0)