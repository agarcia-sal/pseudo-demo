from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        mod = 10**9 + 7
        L = defaultdict(int)
        M = defaultdict(int)

        for a in nums:
            # Ensure keys exist with default 0 (redundant due to defaultdict)
            _ = L[a]
            _ = M[a]

            M[a] = (M[a] + 1) % mod
            L[a] = (L[a] + a) % mod

            p = (L[a] + L[a - 1]) % mod
            q = (M[a - 1] * a) % mod
            L[a] = (p + q) % mod

            r = (M[a] + M[a - 1]) % mod
            M[a] = r

            s = (L[a] + L[a + 1]) % mod
            t = (M[a + 1] * a) % mod
            L[a] = (s + t) % mod

            u = (M[a] + M[a + 1]) % mod
            M[a] = u

        total = sum(L.values()) % mod
        return total