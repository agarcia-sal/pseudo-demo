from math import inf
from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def update_count(count_list: List[int], n: int, delta: int) -> None:
            bitmask = 1
            idx = 0
            while idx < 32:
                if (n & bitmask) != 0:
                    count_list[idx] += delta
                bitmask <<= 1
                idx += 1

        def compute_current_or(count_list: List[int]) -> int:
            result_or = 0
            position = 0
            while position < 32:
                if count_list[position] > 0:
                    result_or |= (1 << position)
                position += 1
            return result_or

        length_nums = len(nums)
        bit_counts = [0] * 32
        curr_or_val = 0
        start_idx = 0
        min_len = inf

        end_idx = 0
        while end_idx < length_nums:
            update_count(bit_counts, nums[end_idx], 1)
            curr_or_val |= nums[end_idx]

            while curr_or_val >= k and start_idx <= end_idx:
                if min_len > (end_idx - start_idx + 1):
                    min_len = end_idx - start_idx + 1
                update_count(bit_counts, nums[start_idx], -1)
                curr_or_val = compute_current_or(bit_counts)
                start_idx += 1
            end_idx += 1

        return -1 if min_len == inf else min_len