from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    """Return True if the sequence is monotonic (either non-decreasing or non-increasing)."""
    # Check if sequence is sorted in non-decreasing order or non-increasing order
    return not (sequence > sorted(sequence)) or not (sorted(sequence, reverse=True) > sequence)