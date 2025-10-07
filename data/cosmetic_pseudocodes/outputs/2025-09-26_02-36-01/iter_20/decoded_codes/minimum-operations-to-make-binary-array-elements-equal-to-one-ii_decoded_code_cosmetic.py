class Solution:
    def minOperations(self, nums):
        def modTwo(value):
            return value - (value // 2) * 2  # Equivalent to value % 2

        alpha = 0
        beta = 0
        gamma = 0

        while gamma < len(nums):
            delta = nums[gamma]
            epsilon = 0

            if modTwo(beta) == 0:
                epsilon = delta
            else:
                epsilon = 1 - delta

            if epsilon == 0:
                alpha += 1
                beta += 1

            gamma += 1

        return alpha