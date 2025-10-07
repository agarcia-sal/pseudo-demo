from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(x: Sequence[T]) -> bool:
    a = sorted(x)
    b = sorted(x, reverse=True)
    return list(x) == a or list(x) == b