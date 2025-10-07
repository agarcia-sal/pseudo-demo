from typing import Sequence

def solution(collection: Sequence[int]) -> int:
    accumulator: int = 0
    position: int = 0
    length: int = len(collection)
    while position < length:
        element = collection[position]
        if (position % 2 == 0) and (element % 2 == 1):
            accumulator += element
        position += 1
    return accumulator