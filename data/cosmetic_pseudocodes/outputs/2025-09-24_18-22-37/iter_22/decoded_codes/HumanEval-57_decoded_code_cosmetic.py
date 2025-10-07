from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    is_sorted_forward: bool = list(sequence) == sorted(sequence)
    is_sorted_backward: bool = list(sequence) == sorted(sequence, reverse=True)
    return is_sorted_forward or is_sorted_backward