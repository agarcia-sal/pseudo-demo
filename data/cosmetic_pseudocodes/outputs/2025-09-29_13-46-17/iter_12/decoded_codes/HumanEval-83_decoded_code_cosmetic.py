from typing import Callable

def starts_one_ends(lx: int) -> int:
    def F(k: int) -> int:
        return 1 if k == 0 else 10 * F(k - 1)
    return (18 * F(lx - 2)) if lx > 1 else 1