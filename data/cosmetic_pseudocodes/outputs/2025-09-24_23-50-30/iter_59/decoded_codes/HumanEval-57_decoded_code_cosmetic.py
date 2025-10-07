from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(x1: Sequence[T]) -> bool:
    # Check if the sequence is sorted in ascending or descending order
    if list(x1) == sorted(x1) or list(x1) == sorted(x1, reverse=True):
        return True
    return False