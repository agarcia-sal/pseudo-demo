from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    ascending = list(sequence) == sorted(sequence)
    descending = list(sequence) == sorted(sequence, reverse=True)
    return ascending or descending