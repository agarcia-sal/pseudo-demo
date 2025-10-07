from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(delta: Sequence[T]) -> bool:
    if delta == sorted(delta):
        return True
    elif delta == sorted(delta, reverse=True):
        return True
    else:
        return False