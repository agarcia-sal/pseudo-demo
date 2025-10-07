from typing import List

def solution(sequence: List[int]) -> int:
    def accumulate(accumulator: int, position: int) -> int:
        if position >= len(sequence):
            return accumulator
        if (position % 2 == 0) and (sequence[position] % 2 == 1):
            return accumulate(accumulator + sequence[position], position + 1)
        return accumulate(accumulator, position + 1)

    return accumulate(0, 0)