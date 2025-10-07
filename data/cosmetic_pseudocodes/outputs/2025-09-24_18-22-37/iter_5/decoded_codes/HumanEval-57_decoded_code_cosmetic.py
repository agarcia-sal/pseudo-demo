from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    sorted_seq_forward = sorted(sequence)
    sorted_seq_reverse = sorted(sequence, reverse=True)
    is_forward_sorted = sequence == sorted_seq_forward
    is_reverse_sorted = sequence == sorted_seq_reverse
    if is_forward_sorted:
        return True
    if is_reverse_sorted:
        return True
    return False