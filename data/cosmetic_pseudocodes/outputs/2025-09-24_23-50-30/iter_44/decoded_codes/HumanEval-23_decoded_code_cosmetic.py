from typing import Iterable

def strlen(foil: Iterable) -> int:
    total: int = 0
    for _ in foil:
        total += 1
    return total