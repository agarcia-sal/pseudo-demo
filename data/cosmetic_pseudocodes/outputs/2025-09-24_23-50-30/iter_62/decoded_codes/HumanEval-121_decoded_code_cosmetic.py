from typing import List

def solution(numerical_sequence: List[int]) -> int:
    def helper(position: int, accumulated_sum: int) -> int:
        if position >= len(numerical_sequence):
            return accumulated_sum
        if position % 2 == 0 and numerical_sequence[position] % 2 == 1:
            return helper(position + 1, accumulated_sum + numerical_sequence[position])
        return helper(position + 1, accumulated_sum)
    return helper(0, 0)