from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    return list(sequence) == sorted(sequence) or list(sequence) == sorted(sequence, reverse=True)