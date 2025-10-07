from typing import List

def add(array_of_nums: List[int]) -> int:
    accumulator: int = 0
    index: int = 1
    while index < len(array_of_nums):
        if array_of_nums[index] % 2 == 0:
            accumulator += array_of_nums[index]
        index += 2
    return accumulator