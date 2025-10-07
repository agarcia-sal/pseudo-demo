class Solution:
    def maximumLength(self, nums):
        a1 = 0
        b2 = 0
        c3 = 1
        while c3 < len(nums):
            d4 = nums[c3 - 1] + nums[c3]
            if d4 % 2 == 0:
                a1 = max(a1 + 1, b2)
            else:
                b2 = max(b2 + 1, a1)
            c3 += 1
        return max(a1, b2) + 1