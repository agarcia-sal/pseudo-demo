from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    # Check if the sequence is sorted in ascending or descending order
    if list(sequence) == sorted(sequence):
        return True
    if list(sequence) == sorted(sequence, reverse=True):
        return True
    return False