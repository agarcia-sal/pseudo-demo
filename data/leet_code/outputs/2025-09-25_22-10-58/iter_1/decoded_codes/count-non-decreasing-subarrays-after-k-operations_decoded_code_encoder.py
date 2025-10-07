class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)

        def canMakeNonDecreasing(start, length):
            cost = 0
            current_max = nums[start]
            for i in range(1, length):
                if nums[start + i] < current_max:
                    cost += current_max - nums[start + i]
                current_max = max(current_max, nums[start + i])
                if cost > k:
                    return False
            return True

        total_subarrays = n * (n + 1) // 2
        invalid_subarrays = 0

        for start in range(n):
            left, right = 1, n - start
            while left <= right:
                mid = (left + right) // 2
                if canMakeNonDecreasing(start, mid):
                    left = mid + 1
                else:
                    right = mid - 1
            invalid_subarrays += n - start - right

        return total_subarrays - invalid_subarrays