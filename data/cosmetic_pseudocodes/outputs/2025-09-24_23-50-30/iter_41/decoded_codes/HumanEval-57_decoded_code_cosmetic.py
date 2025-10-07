from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    return sequence == sorted(sequence) or sequence == sorted(sequence, reverse=True)