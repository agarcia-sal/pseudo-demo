from typing import Sequence, TypeVar

T = TypeVar('T', covariant=True)

def monotonic(sequence: Sequence[T]) -> bool:
    """Return True if sequence is monotonic (entirely non-decreasing or non-increasing)."""
    return sequence == sorted(sequence) or sequence == sorted(sequence, reverse=True)