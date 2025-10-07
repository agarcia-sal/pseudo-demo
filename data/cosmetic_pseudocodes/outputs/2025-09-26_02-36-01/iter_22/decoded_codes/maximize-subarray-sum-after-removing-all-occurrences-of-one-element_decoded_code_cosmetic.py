from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        def kadane(arr: List[int]) -> int:
            max_current = max_global = arr[0]
            for x in arr[1:]:
                max_current = x if max_current + x < x else max_current + x
                if max_global < max_current:
                    max_global = max_current
            return max_global

        max_sum = kadane(nums)
        unique_nums = set(nums)

        for val in unique_nums:
            filtered = [x for x in nums if x != val]
            if filtered:
                candidate = kadane(filtered)
                if max_sum < candidate:
                    max_sum = candidate

        return max_sum