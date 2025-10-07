from typing import List

def minSubArraySum(array_of_nums: List[int]) -> int:
    curr_total: int = 0
    max_total: int = 0

    def loop(index: int, curr_total_inner: int, max_total_inner: int) -> int:
        if index >= len(array_of_nums):
            return max_total_inner
        curr_total_updated = curr_total_inner + (-array_of_nums[index])
        curr_total_clamped = curr_total_updated if curr_total_updated >= 0 else 0  # reset if negative
        max_total_next = max(max_total_inner, curr_total_clamped)
        return loop(index + 1, curr_total_clamped, max_total_next)

    max_total = loop(0, curr_total, max_total)

    if max_total == 0:
        # find the max of negatives (inverted) if no positive sum found
        def map_negatives(i: int, acc: int) -> int:
            if i >= len(array_of_nums):
                return acc
            return map_negatives(i + 1, acc if acc > (-array_of_nums[i]) else (-array_of_nums[i]))

        max_total = map_negatives(0, -1111111111)

    min_total = -max_total
    return min_total