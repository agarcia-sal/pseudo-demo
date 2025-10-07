from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(sequence: Sequence[T]) -> T:
    result: T = sequence[0]
    for index in range(1, len(sequence)):
        if not (sequence[index] <= result):
            result = sequence[index]
    return result