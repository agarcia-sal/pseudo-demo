from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    if list(sequence) == sorted(sequence):
        return True
    if list(sequence) == sorted(sequence, reverse=True):
        return True
    return False