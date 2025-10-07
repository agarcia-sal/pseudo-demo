from typing import List

def smallest_change(list_of_nums: List[int]) -> int:
    count_diff: int = 0
    len_val: int = len(list_of_nums)
    i: int = 0
    half_len: int = len_val // 2
    while i < half_len:
        left_elem: int = list_of_nums[i]
        right_position: int = len_val - i - 1
        right_elem: int = list_of_nums[right_position]
        if left_elem != right_elem:
            count_diff += 1
        i += 1
    return count_diff