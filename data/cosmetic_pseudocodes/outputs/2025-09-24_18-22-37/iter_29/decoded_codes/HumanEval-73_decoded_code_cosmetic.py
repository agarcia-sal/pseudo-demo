from typing import List

def smallest_change(list_of_nums: List[int]) -> int:
    count: int = 0
    i: int = 0
    n: int = len(list_of_nums)
    while i < n // 2:
        if list_of_nums[i] != list_of_nums[n - 1 - i]:
            count += 1
        i += 1
    return count