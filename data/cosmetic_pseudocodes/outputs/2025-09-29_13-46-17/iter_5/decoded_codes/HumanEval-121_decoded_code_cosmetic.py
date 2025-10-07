from typing import List

def solution(numbers: List[int]) -> int:
    def recursiveSum(position: int, accumulator: int) -> int:
        if position >= len(numbers):
            return accumulator
        value = numbers[position]
        updatedAcc = accumulator + (value if position % 2 == 0 and value % 2 == 1 else 0)
        return recursiveSum(position + 1, updatedAcc)
    return recursiveSum(0, 0)