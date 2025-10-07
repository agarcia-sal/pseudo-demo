from typing import Sequence

def solution(data_collection: Sequence[int]) -> int:
    accumulator: int = 0
    position: int = 0
    while position < len(data_collection):
        if (position % 2 == 0) and (data_collection[position] % 2 == 1):
            accumulator += data_collection[position]
        position += 1
    return accumulator