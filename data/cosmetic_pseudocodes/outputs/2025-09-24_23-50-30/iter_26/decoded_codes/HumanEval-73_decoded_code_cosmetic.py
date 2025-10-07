from typing import List

def smallest_change(list_of_nums: List[int]) -> int:
    counter = 0

    def helper(pos: int, limit: int) -> int:
        nonlocal counter
        if pos > limit:
            return counter
        if list_of_nums[pos] != list_of_nums[(limit * 2 + 1) - pos - 1]:
            counter += 1
        return helper(pos + 1, limit)

    return helper(0, len(list_of_nums) // 2 - 1)