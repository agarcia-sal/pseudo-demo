from typing import Iterable

def exchange(alpha: Iterable[int], beta: Iterable[int]) -> str:
    psi: int = 0
    omega: int = 0

    for x in alpha:
        if x % 2 == 1:
            psi += 1

    for y in beta:
        if y % 2 == 0:
            omega += 1

    if omega >= psi:
        return "YES"
    else:
        return "NO"