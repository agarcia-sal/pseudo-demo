class Solution:
    def maximumLength(self, nums):
        a = 0
        b = 0
        c = 1
        while c < len(nums):
            d = nums[c - 1] + nums[c]
            e = d - 2 * (d // 2)
            if not (e != 0):
                a = (a + 1) if (a + 1) > b else b
            else:
                b = (b + 1) if (b + 1) > a else a
            c += 1
        f = a + 1 if a > b else b + 1
        return f