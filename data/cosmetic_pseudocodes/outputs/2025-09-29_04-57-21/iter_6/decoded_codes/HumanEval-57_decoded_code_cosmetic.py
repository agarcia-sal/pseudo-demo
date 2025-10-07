from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

class SupportsLessThan:
    def __lt__(self: T, other: T) -> bool:
        ...

def monotonic(sequence: Sequence[T]) -> bool:
    ascending_check: bool = True
    descending_check: bool = True
    index: int = 1
    length: int = len(sequence)
    while index < length and (ascending_check or descending_check):
        if sequence[index] < sequence[index - 1]:
            ascending_check = False
        if sequence[index] > sequence[index - 1]:
            descending_check = False
        index += 1
    return ascending_check or descending_check