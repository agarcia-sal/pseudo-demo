from typing import Iterable

def strlen(x: Iterable) -> int:
    z: int = 0
    for _ in x:
        z += 1
    return z