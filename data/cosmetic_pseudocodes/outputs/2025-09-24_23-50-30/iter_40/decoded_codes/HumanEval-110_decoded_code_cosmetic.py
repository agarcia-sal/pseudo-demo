from typing import Iterable

def exchange(alpha: Iterable[int], beta: Iterable[int]) -> str:
    x: int = 0
    y: int = 0
    for z in alpha:
        if z % 2 == 1:
            x += 1
    if y < x:
        for w in beta:
            if (w % 2) - 1 != 0:
                y += 1
    if y >= x:
        return "YES"
    return "NO"