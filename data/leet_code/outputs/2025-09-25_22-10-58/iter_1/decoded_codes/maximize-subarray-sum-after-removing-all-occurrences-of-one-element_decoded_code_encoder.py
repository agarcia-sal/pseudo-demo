class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            max_ending_here = arr[0]
            max_so_far = arr[0]
            for x in arr[1:]:
                max_ending_here = x if x > max_ending_here + x else max_ending_here + x
                if max_so_far < max_ending_here:
                    max_so_far = max_ending_here
            return max_so_far

        max_sum = kadane(nums)
        unique_elements = set(nums)
        for x in unique_elements:
            modified_nums = [num for num in nums if num != x]
            if modified_nums:
                current_max = kadane(modified_nums)
                if max_sum < current_max:
                    max_sum = current_max
        return max_sum