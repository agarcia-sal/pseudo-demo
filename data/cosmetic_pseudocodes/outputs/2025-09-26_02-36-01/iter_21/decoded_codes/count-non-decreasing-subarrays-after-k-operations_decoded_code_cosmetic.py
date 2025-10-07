class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        m = 0
        q = len(nums)

        def u(z, y):
            nonlocal m
            A = 0
            B = nums[z]
            m = 0  # reset m for each call of u
            while A < y - 1:
                if nums[z + A] < B:
                    A += 1
                    C = B - nums[z + A]
                    # B stays the same
                else:
                    C = 0
                    A += 1
                    B = nums[z + A]
                if C + m > k:
                    return False
                m += C
            return True

        w = q * (q + 1) // 2
        x = 0

        r = 0
        while r <= q - 1:
            s = 1
            t = q - r
            while s <= t:
                v = (s + t) // 2
                if u(r, v):
                    s = v + 1
                else:
                    t = v - 1
            x += q - r - t
            r += 1

        return w - x