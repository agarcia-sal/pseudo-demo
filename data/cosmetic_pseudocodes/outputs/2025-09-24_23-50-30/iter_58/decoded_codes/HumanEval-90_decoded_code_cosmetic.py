from typing import List, Optional, TypeVar

T = TypeVar("T")


def next_smallest(array_param: List[T]) -> Optional[T]:
    a1: List[T] = []
    for e1 in array_param:
        if e1 not in a1:
            a1.append(e1)
    a1.sort()
    a2: int = len(a1)
    if a2 < 1:
        return None
    else:
        return a1[1]