from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence_container: Sequence[T]) -> bool:
    # Check if sequence is sorted either ascending or descending
    return sequence_container == sorted(sequence_container) or sequence_container == sorted(sequence_container, reverse=True)