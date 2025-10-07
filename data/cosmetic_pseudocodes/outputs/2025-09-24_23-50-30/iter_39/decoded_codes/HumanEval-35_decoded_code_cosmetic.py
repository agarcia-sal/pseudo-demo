from typing import Sequence, TypeVar

T = TypeVar('T')


def max_element(sequence: Sequence[T]) -> T:
    accumulator: T = sequence[0]
    iterator: int = 1
    while iterator < len(sequence):
        if not (sequence[iterator] <= accumulator):
            accumulator = sequence[iterator]
        iterator += 1
    return accumulator