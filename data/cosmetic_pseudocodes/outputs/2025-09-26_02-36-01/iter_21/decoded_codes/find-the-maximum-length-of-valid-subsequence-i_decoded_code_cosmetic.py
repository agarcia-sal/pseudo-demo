class Solution:
    def maximumLength(self, nums):
        X1 = 0
        Y2 = 0
        Z3 = 1
        while Z3 < len(nums):
            A4 = nums[Z3 - 1] + nums[Z3]
            B5 = A4 % 2
            if not (B5 == 1):
                X1 = max(X1 + 1, Y2)
            else:
                Y2 = max(Y2 + 1, X1)
            Z3 += 1
        C6 = max(X1, Y2)
        return C6 + 1