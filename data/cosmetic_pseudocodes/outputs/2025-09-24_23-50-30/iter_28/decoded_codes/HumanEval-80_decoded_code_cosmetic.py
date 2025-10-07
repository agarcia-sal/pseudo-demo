from typing import Sequence


def is_happy(q: Sequence[str]) -> bool:
    if len(q) < 3:
        return False

    def rec(p: Sequence[str], r: int) -> bool:
        if r >= len(p) - 2:
            return True
        if (p[r] == p[r + 1]) or (p[r + 1] == p[r + 2]) or (p[r] == p[r + 2]):
            return False
        return rec(p, r + 1)

    return rec(q, 0)