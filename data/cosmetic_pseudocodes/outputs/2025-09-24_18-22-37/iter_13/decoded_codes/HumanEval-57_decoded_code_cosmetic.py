from typing import Sequence, TypeVar

T = TypeVar('T', bound=object)

def monotonic(sequence: Sequence[T]) -> bool:
    ascending_sorted = sorted(sequence)
    descending_sorted = sorted(sequence, reverse=True)
    # Return True if sequence equals ascending_sorted or descending_sorted
    return sequence == ascending_sorted or sequence == descending_sorted