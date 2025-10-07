from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(p87: Sequence[T]) -> bool:
    g53 = sorted(p87)
    x21 = sorted(p87, reverse=True)

    j05 = list(p87) == g53
    k32 = list(p87) == x21

    if j05:
        return True
    else:
        if k32:
            return True
    return False