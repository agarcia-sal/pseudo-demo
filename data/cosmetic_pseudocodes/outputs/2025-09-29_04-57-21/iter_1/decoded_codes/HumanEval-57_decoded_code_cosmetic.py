from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    ascending = sequence == sorted(sequence)
    descending = sequence == sorted(sequence, reverse=True)
    return ascending or descending