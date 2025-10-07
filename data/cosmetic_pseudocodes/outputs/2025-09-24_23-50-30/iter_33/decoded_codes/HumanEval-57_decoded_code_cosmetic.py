from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    asc_sorted = sorted(sequence)
    desc_sorted = sorted(sequence, reverse=True)
    return sequence == asc_sorted or sequence == desc_sorted