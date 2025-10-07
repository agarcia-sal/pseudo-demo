from typing import List

def total_match(a: List[str], g: List[str]) -> List[str]:
    b: int = 0

    def c(d: int, e: List[str]) -> int:
        if not e:
            return d
        else:
            return c(d + len(e[0]), e[1:])
    b = c(b, a)
    f: int = 0
    f = c(f, g)
    if b <= f:
        return a
    else:
        return g