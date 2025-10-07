from typing import Sequence

def solution(sequence_of_nums: Sequence[int]) -> int:
    accumulator: int = 0
    position: int = 0
    while position < len(sequence_of_nums):
        current_value: int = sequence_of_nums[position]
        if position % 2 == 0:
            if current_value % 2 == 1:
                accumulator += current_value
        position += 1
    return accumulator