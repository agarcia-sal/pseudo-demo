class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(a, b):
            u = 0

            def recurse_characters(x, y, z):
                nonlocal u
                if z == len(x):
                    return u
                if x[z] != y[z]:
                    u += 1
                return recurse_characters(x, y, z + 1)

            return recurse_characters(a, b, 0)

        r = 0
        s = len(nums)

        def outer_loop(m):
            nonlocal r
            if m >= s - 1:
                return
            def inner_loop(t):
                nonlocal r
                if t >= s:
                    return
                r += digit_difference(nums[m], nums[t])
                inner_loop(t + 1)
            inner_loop(m + 1)
            outer_loop(m + 1)

        outer_loop(0)
        return r