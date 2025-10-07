from typing import List

def solution(array_of_nums: List[int]) -> int:
    total_sum: int = 0
    position_counter: int = 0
    while position_counter < len(array_of_nums):
        current_element = array_of_nums[position_counter]
        if (position_counter % 2) == 0 and (current_element % 2) == 1:
            total_sum += current_element
        position_counter += 1
    return total_sum