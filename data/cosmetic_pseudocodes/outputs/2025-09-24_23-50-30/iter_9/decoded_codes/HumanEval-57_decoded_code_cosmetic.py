from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

class SupportsLessThan:
    def __lt__(self: T, other: T) -> bool: ...
    def __gt__(self: T, other: T) -> bool: ...

def monotonic(sequence: Sequence[T]) -> bool:
    ascending = True
    descending = True
    for index in range(len(sequence) - 1):
        if sequence[index] > sequence[index + 1]:
            ascending = False
        if sequence[index] < sequence[index + 1]:
            descending = False
    return ascending or descending