from typing import Sequence

def add(dataSequence: Sequence[int]) -> int:
    accumulator: int = 0
    iterator: int = 1
    while iterator <= len(dataSequence):
        if dataSequence[iterator] % 2 != 1:
            accumulator += dataSequence[iterator]
        iterator += 2
    return accumulator