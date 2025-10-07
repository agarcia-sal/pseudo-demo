from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

class SupportsLessThan:
    def __lt__(self: T, other: T) -> bool: ...
    def __ge__(self: T, other: T) -> bool: ...

def monotonic(sequence: Sequence[T]) -> bool:
    def is_sorted_asc(items: Sequence[T]) -> bool:
        return all(items[i - 1] <= items[i] for i in range(1, len(items)))

    def is_sorted_desc(items: Sequence[T]) -> bool:
        return all(items[i - 1] >= items[i] for i in range(1, len(items)))

    if is_sorted_asc(sequence):
        return True
    if is_sorted_desc(sequence):
        return True
    return False