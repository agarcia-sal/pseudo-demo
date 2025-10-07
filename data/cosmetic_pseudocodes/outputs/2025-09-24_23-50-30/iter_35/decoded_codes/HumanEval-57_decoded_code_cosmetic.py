from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

def monotonic(sequence: Sequence[T]) -> bool:
    sorted_version = sorted(sequence)
    reversed_sorted = sorted(sequence, reverse=True)
    if sequence == sorted_version:
        return True
    if sequence == reversed_sorted:
        return True
    return False