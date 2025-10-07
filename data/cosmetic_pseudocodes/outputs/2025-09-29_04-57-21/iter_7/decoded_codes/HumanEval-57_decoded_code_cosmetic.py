from typing import Sequence, TypeVar

T = TypeVar("T")

def monotonic(sequence_of_items: Sequence[T]) -> bool:
    # Check if the sequence is sorted ascending or descending
    return (sequence_of_items == sorted(sequence_of_items) or
            sequence_of_items == sorted(sequence_of_items, reverse=True))