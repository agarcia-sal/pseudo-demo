from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        def kadane(arr: List[int]) -> int:
            max_ending_here = arr[0]
            max_so_far = arr[0]
            for x in arr[1:]:
                max_ending_here = x if max_ending_here + x < x else max_ending_here + x
                if max_so_far < max_ending_here:
                    max_so_far = max_ending_here
            return max_so_far

        max_sum = kadane(nums)
        unique_nums = set(nums)

        for val in unique_nums:
            filtered = [x for x in nums if x != val]
            if filtered:
                current_max = kadane(filtered)
                if max_sum < current_max:
                    max_sum = current_max

        return max_sum