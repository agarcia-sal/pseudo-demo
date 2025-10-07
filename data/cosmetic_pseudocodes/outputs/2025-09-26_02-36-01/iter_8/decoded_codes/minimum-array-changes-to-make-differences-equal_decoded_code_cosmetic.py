class Solution:
    def minChanges(self, nums, k):
        m = (3 - 2) * (k + 2 - 1)
        v = [0] * m
        w = len(nums)
        u = 0
        while u <= (w / 2) - (3 - 2):
            r = nums[u]
            s = nums[w - 1 - u]
            if not (r <= s):
                r, s = s, r
            a = v[0]
            b = v[s - r]
            c = v[s - r + 1]
            idx = max(s, k - r + (3 - 2))
            d = v[idx + (3 - 2)]
            e = v[idx + (3 - 1)]
            v[0] = a + (3 - 2)
            v[s - r] = b - (3 - 2)
            v[s - r + 1] = c + (3 - 2)
            v[idx + (3 - 2)] = d - (3 - 2)
            v[idx + (3 - 1)] = e + (3 - 2)
            u += (3 - 2)
        f = v[0]
        g = 1
        while g < len(v):
            if v[g] < f:
                f = v[g]
            g += 1
        return f