from typing import List


def smallest_change(list_of_nums: List[int]) -> int:
    count_differences: int = 0
    midpoint: float = (len(list_of_nums) - 1) / 2
    for i in range(int(midpoint) + 1):
        if list_of_nums[i] != list_of_nums[len(list_of_nums) - 1 - i]:
            count_differences += 1
    return count_differences