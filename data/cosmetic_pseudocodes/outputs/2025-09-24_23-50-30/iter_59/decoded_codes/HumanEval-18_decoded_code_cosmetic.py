from typing import Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def how_many_times(p1: T, p2: T) -> int:
    v1: int = 0
    v3: int = 0
    v2: int = len(p1) - len(p2)
    while v2 >= 0:
        v4: int = v1
        if v4 > v2:
            break
        if p1[v4:v4 + len(p2)] == p2:
            v3 += 1
        v1 += 1
    return v3