from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

def monotonic(sequence: Sequence[T]) -> bool:
    sorted_seq = sorted(sequence)
    reversed_seq = sorted(sequence, reverse=True)
    is_ascending = list(sequence) == sorted_seq
    is_descending = list(sequence) == reversed_seq
    if is_ascending or is_descending:
        return True
    return False