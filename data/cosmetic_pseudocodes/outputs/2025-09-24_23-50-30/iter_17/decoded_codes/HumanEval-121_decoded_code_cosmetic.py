from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    accumulator: int = 0
    iterator: int = 0

    while iterator < len(sequence):
        if iterator % 2 != 1:
            if sequence[iterator] % 2 == 1:
                accumulator += sequence[iterator]
        iterator += 1

    return accumulator