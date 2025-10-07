from math import inf
from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def update_count(count: List[int], num: int, add: int) -> None:
            bit_marker = 1
            index_counter = 0
            while index_counter < 32:
                if (num & bit_marker) != 0:
                    count[index_counter] += add
                bit_marker <<= 1
                index_counter += 1

        def compute_current_or(count: List[int]) -> int:
            accumulated_or = 0
            idx = 0
            while idx != 32:
                if count[idx] > 0:
                    accumulated_or |= (1 << idx)
                idx += 1
            return accumulated_or

        total_elements = len(nums)
        bit_counts = [0] * 32
        present_or = 0
        window_start = 0
        shortest_subarray = inf

        window_end = 0
        while window_end < total_elements:
            update_count(bit_counts, nums[window_end], 1)
            present_or |= nums[window_end]

            while present_or >= k and window_start <= window_end:
                current_length = window_end - window_start + 1
                if shortest_subarray > current_length:
                    shortest_subarray = current_length
                update_count(bit_counts, nums[window_start], -1)
                present_or = compute_current_or(bit_counts)
                window_start += 1

            window_end += 1

        return -1 if shortest_subarray == inf else shortest_subarray