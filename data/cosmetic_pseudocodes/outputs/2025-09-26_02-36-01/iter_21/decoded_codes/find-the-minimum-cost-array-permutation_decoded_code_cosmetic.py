class Solution:
    def findPermutation(self, nums):
        n = len(nums)
        full_mask = (1 << n) - 1
        ans = []

        def u70(k4x, m9z):
            if (k4x ^ full_mask) == 0:
                pre0 = m9z - nums[0]
                return abs(pre0)
            v32 = float('inf')
            for idx in range(n):
                if ((k4x >> idx) & 1) == 0:
                    wv = m9z - nums[idx]
                    ua = abs(wv) + u70(k4x | (1 << idx), idx)
                    if ua < v32:
                        v32 = ua
            return v32

        def kz(k4x, m9z):
            ans.append(m9z)
            if (k4x ^ full_mask) == 0:
                return
            v32 = u70(k4x, m9z)
            curi = 0
            while curi < n:
                if ((k4x >> curi) & 1) == 0:
                    wv = m9z - nums[curi]
                    ua = abs(wv) + u70(k4x | (1 << curi), curi)
                    if ua == v32:
                        kz(k4x | (1 << curi), curi)
                        break
                curi += 1

        kz(1 << 0, 0)
        return ans