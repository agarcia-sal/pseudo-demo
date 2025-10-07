from typing import Sequence, TypeVar

T = TypeVar('T', bound=object)

def monotonic(arrangement: Sequence[T]) -> bool:
    return arrangement == sorted(arrangement) or arrangement == sorted(arrangement, reverse=True)