from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

def monotonic(array_sequence: Sequence[T]) -> bool:
    temp_sorted_forward = sorted(array_sequence)
    temp_sorted_reverse = sorted(array_sequence, reverse=True)
    condition_one = list(array_sequence) == temp_sorted_forward
    condition_two = list(array_sequence) == temp_sorted_reverse
    return condition_one or condition_two