class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(a, b):
            r = 0
            c = 0
            while c < len(a):
                if a[c] != b[c]:
                    r += 1
                c += 1
            return r

        u = 0
        v = len(nums)
        w = 0
        while w < v:
            x = w + 1
            while x < v:
                u += digit_difference(nums[w], nums[x])
                x += 1
            w += 1
        return u