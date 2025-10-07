from typing import Iterable

def solution(collection_of_numbers: Iterable[int]) -> int:
    accumulation: int = 0
    position: int = 0
    nums = list(collection_of_numbers)  # To allow indexing

    while position < len(nums):
        element = nums[position]
        if (position % 2 == 0) and (element % 2 != 0):
            accumulation += element
        position += 1

    return accumulation