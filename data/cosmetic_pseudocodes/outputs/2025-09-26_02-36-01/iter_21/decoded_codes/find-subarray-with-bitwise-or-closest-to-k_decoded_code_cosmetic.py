class Solution:
    def minimumDifference(self, nums, k):
        m = len(nums)
        z = float('inf')

        p = 0
        while p < m:
            q = 0
            r = p
            while r < m:
                q |= nums[r]
                s = k - q
                if s < 0:
                    s = -s
                if s < z:
                    z = s
                if s == 0:
                    return 0
                r += 1
            p += 1
        return z