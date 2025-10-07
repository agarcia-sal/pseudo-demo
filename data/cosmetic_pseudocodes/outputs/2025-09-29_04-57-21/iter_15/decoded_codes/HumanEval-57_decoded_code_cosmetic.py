from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    is_asc = list(sequence) == sorted(sequence)
    is_desc = list(sequence) == sorted(sequence, reverse=True)
    if not (is_asc or is_desc):
        return False
    return True