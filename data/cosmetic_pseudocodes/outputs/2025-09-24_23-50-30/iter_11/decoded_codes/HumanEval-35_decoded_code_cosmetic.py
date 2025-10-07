from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(sequence: Sequence[T]) -> T:
    index: int = 1
    highest: T = sequence[0]
    while index < len(sequence):
        current = sequence[index]
        if current > highest:
            highest = current
        index += 1
    return highest