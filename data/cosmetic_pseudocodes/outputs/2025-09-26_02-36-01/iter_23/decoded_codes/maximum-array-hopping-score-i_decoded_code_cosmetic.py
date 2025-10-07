class Solution:
    def maxScore(self, nums):
        length = len(nums)
        y9 = [0] * length

        def helper(a, b, c):
            return a + (b - c) * nums[b]

        def recur(p7):
            if p7 > length - 1:
                return
            def inner_loop(q4):
                if q4 >= p7:
                    return
                if not (y9[p7] >= helper(y9[q4], p7, q4)):
                    y9[p7] = y9[q4] + (p7 - q4) * nums[p7]
                inner_loop(q4 + 1)
            inner_loop(0)
            recur(p7 + 1)

        recur(1)
        return y9[length - 1]