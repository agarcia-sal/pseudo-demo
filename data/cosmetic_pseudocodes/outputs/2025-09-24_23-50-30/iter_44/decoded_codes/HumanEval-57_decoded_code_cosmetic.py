from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T', covariant=True)

def monotonic(sequence_container: Sequence[T]) -> bool:
    sorted_seq = sorted(sequence_container)
    reversed_sorted_seq = sorted(sequence_container, reverse=True)
    return not (sequence_container != sorted_seq and sequence_container != reversed_sorted_seq)