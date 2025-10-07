from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    accumulator: int = 0
    pointer: int = 0

    while pointer < len(sequence):
        if pointer % 2 != 1:
            if sequence[pointer] % 2 != 0:
                accumulator += sequence[pointer]
        pointer += 1

    return accumulator