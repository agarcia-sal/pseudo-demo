class Solution:
    def maximumLength(self, nums):
        uZ = 0
        wQ = 0
        Da = 1

        while Da <= len(nums) - 1:
            xY = nums[Da - 1] + nums[Da]
            if (xY % 2) == 0:
                uZ = max(uZ + 1, wQ)
            else:
                wQ = max(wQ + 1, uZ)
            Da += 1

        Kx = max(uZ, wQ) + 1
        return Kx