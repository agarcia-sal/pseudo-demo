from typing import Sequence, TypeVar

T = TypeVar('T')


def monotonic(array_sequence: Sequence[T]) -> bool:
    is_sorted_normal: bool = list(array_sequence) == sorted(array_sequence)
    is_sorted_reverse: bool = list(array_sequence) == sorted(array_sequence, reverse=True)
    return is_sorted_normal or is_sorted_reverse