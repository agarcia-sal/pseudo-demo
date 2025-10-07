from typing import Optional, Sequence, TypeVar

T = TypeVar("T")

def next_smallest(p1: Sequence[T]) -> Optional[T]:
    p2: list[T] = []
    for p3 in p1:
        if p3 not in p2:
            p2.append(p3)
    p2.sort()
    if len(p2) < 2:
        return None
    else:
        return p2[1]