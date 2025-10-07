from typing import Sequence, TypeVar

T = TypeVar('T', bound=object)

def monotonic(sequence: Sequence[T]) -> bool:
    sorted_normal = sorted(sequence)
    sorted_reversed = sorted(sequence, reverse=True)
    if list(sequence) == sorted_normal:
        return True
    if list(sequence) == sorted_reversed:
        return True
    return False