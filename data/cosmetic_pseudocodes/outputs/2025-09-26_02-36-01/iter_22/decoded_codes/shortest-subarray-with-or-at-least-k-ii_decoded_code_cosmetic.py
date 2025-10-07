from math import inf
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def update_count(count: List[int], num: int, add: int) -> None:
            bit_mask = 1
            idx = 0
            while idx < 32:
                if num & bit_mask != 0:
                    count[idx] += add
                bit_mask <<= 1
                idx += 1

        def compute_current_or(count: List[int]) -> int:
            res = 0
            pos = 0
            while pos < 32:
                if count[pos] > 0:
                    res |= (1 << pos)
                pos += 1
            return res

        size = len(nums)
        tally = [0] * 32
        overall_or = 0
        start_idx = 0
        best_len = inf

        curr_idx = 0
        while curr_idx < size:
            update_count(tally, nums[curr_idx], 1)
            overall_or |= nums[curr_idx]

            while overall_or >= k and start_idx <= curr_idx:
                curr_len = curr_idx - start_idx + 1
                if best_len > curr_len:
                    best_len = curr_len
                update_count(tally, nums[start_idx], -1)
                overall_or = compute_current_or(tally)
                start_idx += 1

            curr_idx += 1

        return -1 if best_len == inf else best_len