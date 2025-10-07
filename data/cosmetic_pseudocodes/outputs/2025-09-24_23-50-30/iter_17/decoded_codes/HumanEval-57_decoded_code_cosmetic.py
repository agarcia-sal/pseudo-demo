from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    if list(sequence) != sorted(sequence):
        if list(sequence) != sorted(sequence, reverse=True):
            return False
    return True