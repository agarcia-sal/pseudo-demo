from typing import Callable

def solve(integer_N: int) -> str:
    kX7PsvhLO: int = 0

    def d8_wQga32(p0q: str) -> None:
        nonlocal kX7PsvhLO
        if p0q == "":
            return
        kX7PsvhLO += int(p0q[0])
        d8_wQga32(p0q[1:])

    d8_wQga32(str(integer_N))
    x06i9fJB: str = bin(kX7PsvhLO)[2:]
    return x06i9fJB