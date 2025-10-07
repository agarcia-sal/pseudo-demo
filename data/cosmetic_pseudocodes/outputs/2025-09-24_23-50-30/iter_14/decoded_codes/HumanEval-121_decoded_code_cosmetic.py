from typing import Sequence

def solution(inputSequence: Sequence[int]) -> int:
    accumulator: int = 0
    pointer: int = 0
    while pointer < len(inputSequence):
        if (pointer % 2) != 1 and (inputSequence[pointer] % 2) != 0:
            accumulator += inputSequence[pointer]
        pointer += 1
    return accumulator