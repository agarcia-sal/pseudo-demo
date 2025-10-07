class Solution:
    def maximumLength(self, nums):
        def modCheck(a, b):
            return a - (a // b) * b

        def maxVal(x, y):
            if x > y:
                return x
            return y

        alpha = 0
        beta = 0
        z = 1

        while z < len(nums):
            tempSum = nums[z - 1] + nums[z]
            if modCheck(tempSum, 2) == 0:
                alpha = maxVal(alpha + 1, beta)
            else:
                beta = maxVal(beta + 1, alpha)
            z += 1

        output = maxVal(alpha, beta) + 1
        return output