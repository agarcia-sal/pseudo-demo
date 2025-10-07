from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence_param: Sequence[T]) -> bool:
    sorted_sequence = sorted(sequence_param)
    reversed_sorted_sequence = sorted(sequence_param, reverse=True)
    if sequence_param == sorted_sequence:
        return True
    if sequence_param == reversed_sorted_sequence:
        return True
    return False