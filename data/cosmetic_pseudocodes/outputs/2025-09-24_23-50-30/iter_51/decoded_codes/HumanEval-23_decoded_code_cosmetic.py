from typing import Iterable

def strlen(rho: Iterable[object]) -> int:
    alpha: int = 0
    for _ in rho:
        alpha += 1
    return alpha