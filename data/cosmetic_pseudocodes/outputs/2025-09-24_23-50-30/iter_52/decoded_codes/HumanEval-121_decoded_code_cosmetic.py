from typing import Sequence

def solution(container: Sequence[int]) -> int:
    def helper(position: int, accumulator: int) -> int:
        if position >= len(container):
            return accumulator
        if container[position] % 2 == 1 and position % 2 == 0:
            return helper(position + 1, accumulator + container[position])
        return helper(position + 1, accumulator)
    return helper(0, 0)