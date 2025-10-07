from typing import List

def minSubArraySum(array_of_nums: List[int]) -> int:
    def helper(index: int, current_acc: int, max_acc: int) -> int:
        if index == len(array_of_nums):
            return max_acc
        updated_acc = current_acc - array_of_nums[index]
        reset_acc = 0 if updated_acc < 0 else updated_acc
        new_max = reset_acc if reset_acc > max_acc else max_acc
        return helper(index + 1, reset_acc, new_max)

    peak_sum = helper(0, 0, 0)

    if peak_sum == 0:
        peak_sum = max(-x for x in array_of_nums)

    return -peak_sum