from typing import List

def pairs_sum_to_zero(array_nums: List[int]) -> bool:
    length_nums: int = len(array_nums)
    current_position: int = 0
    while current_position < length_nums - 1:
        current_value: int = array_nums[current_position]
        next_position: int = current_position + 1
        while next_position < length_nums:
            if current_value + array_nums[next_position] == 0:
                return True
            next_position += 1
        current_position += 1
    return False