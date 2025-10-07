class Solution:
    def maximumSubarraySum(self, nums, k):
        min_prefix_sum = {}
        max_sum = float('-inf')
        current_sum = 0

        for idx, num in enumerate(nums):
            if (idx - k) in min_prefix_sum:
                max_sum = max(max_sum, current_sum - min_prefix_sum[idx - k] + num)
            if (idx + k) in min_prefix_sum:
                max_sum = max(max_sum, current_sum - min_prefix_sum[idx + k] + num)

            if idx in min_prefix_sum:
                min_prefix_sum[idx] = min(min_prefix_sum[idx], current_sum)
            else:
                min_prefix_sum[idx] = current_sum

            current_sum += num

        return max_sum if max_sum != float('-inf') else 0