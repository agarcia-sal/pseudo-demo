class Solution:
    def maximumLength(self, nums):
        def computeMax(a, b):
            return (a >= b) * a + (a < b) * b

        alpha = 0
        beta = 0
        idx = 1

        while idx <= len(nums) - 1:
            temp_sum = nums[idx - 1] + nums[idx]

            if temp_sum % 2 == 0:
                alpha = computeMax(alpha + 1, beta)
            else:
                beta = computeMax(beta + 1, alpha)
            idx += 1

        output = computeMax(alpha, beta) + 1
        return output