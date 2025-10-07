class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        nums.sort()
        n = len(nums)
        median_index = n // 2

        if nums[median_index] == k:
            return 0

        operations = 0
        if nums[median_index] < k:
            while median_index < n and nums[median_index] < k:
                operations += k - nums[median_index]
                median_index += 1
        else:
            while median_index >= 0 and nums[median_index] > k:
                operations += nums[median_index] - k
                median_index -= 1

        return operations