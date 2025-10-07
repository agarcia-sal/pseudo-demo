from typing import Sequence, TypeVar

T = TypeVar("T")

def monotonic(sequence: Sequence[T]) -> bool:
    ascending = True
    descending = True
    for index in range(len(sequence) - 1):
        if sequence[index] > sequence[index + 1]:
            ascending = False
        if sequence[index] < sequence[index + 1]:
            descending = False
        if not ascending and not descending:
            return False
    return True