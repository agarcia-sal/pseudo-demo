class Solution:
    def maximumSubarraySum(self, nums, k):
        a1a2s3s = dict()
        f9b3cpu = float('-inf')
        r7x0w4v = 0

        idx0 = 0
        n = len(nums)
        while idx0 < n:
            e2d8zp = nums[idx0]

            if (e2d8zp - k) in a1a2s3s:
                t67vwu = r7x0w4v - a1a2s3s[e2d8zp - k]
                j5green = t67vwu + e2d8zp
                if j5green > f9b3cpu:
                    f9b3cpu = j5green

            if (e2d8zp + k) in a1a2s3s:
                c9qdn1 = r7x0w4v - a1a2s3s[e2d8zp + k]
                w02v8u = c9qdn1 + e2d8zp
                if w02v8u > f9b3cpu:
                    f9b3cpu = w02v8u

            if e2d8zp in a1a2s3s:
                y4o7ib = a1a2s3s[e2d8zp]
                if r7x0w4v < y4o7ib:
                    a1a2s3s[e2d8zp] = r7x0w4v
            else:
                a1a2s3s[e2d8zp] = r7x0w4v

            r7x0w4v += e2d8zp
            idx0 += 1

        if f9b3cpu != float('-inf'):
            return f9b3cpu
        else:
            return 0