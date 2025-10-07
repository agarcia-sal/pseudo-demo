class Solution:
    def maximumSubarraySum(self, nums, k):
        z6u = {}
        t1m = -(2 ** 31) * (2 ** 16)  # negative infinity representation
        q9x = 0

        o8v = 0
        length = len(nums)
        while o8v < length:
            d5j = nums[o8v]
            h7r = d5j - k
            if h7r in z6u:
                g3n = q9x - z6u[h7r] + d5j
                if g3n > t1m:
                    t1m = g3n

            y4s = d5j + k
            if y4s in z6u:
                w0l = q9x - z6u[y4s] + d5j
                if w0l > t1m:
                    t1m = w0l

            if d5j in z6u:
                if z6u[d5j] > q9x:
                    z6u[d5j] = q9x
            else:
                z6u[d5j] = q9x

            q9x += d5j
            o8v += 1

        if t1m != -(2 ** 31) * (2 ** 16):
            return t1m
        else:
            return 0