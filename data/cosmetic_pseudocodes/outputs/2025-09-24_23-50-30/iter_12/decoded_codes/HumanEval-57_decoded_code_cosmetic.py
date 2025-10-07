from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

class SupportsLessThan:
    def __lt__(self: T, other: T) -> bool: ...
    def __gt__(self: T, other: T) -> bool: ...

def monotonic(sequence: Sequence[T]) -> bool:
    def is_sorted_asc(idx: int) -> bool:
        if idx >= len(sequence) - 1:
            return True
        if sequence[idx] > sequence[idx + 1]:
            return False
        return is_sorted_asc(idx + 1)

    def is_sorted_desc(idx: int) -> bool:
        if idx >= len(sequence) - 1:
            return True
        if sequence[idx] < sequence[idx + 1]:
            return False
        return is_sorted_desc(idx + 1)

    # If sequence is not not ascending or not not descending => ascending or descending
    if not (is_sorted_asc(0) is False) or not (is_sorted_desc(0) is False):
        return True
    return False