from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        mod = 10**9 + 7
        f = defaultdict(int)
        g = defaultdict(int)

        for x in nums:
            g[x] = (g[x] + 1) % mod
            f[x] = (f[x] + x) % mod

            f[x] = (f[x] + f[x - 1] + g[x - 1] * x) % mod
            g[x] = (g[x] + g[x - 1]) % mod

            f[x] = (f[x] + f[x + 1] + g[x + 1] * x) % mod
            g[x] = (g[x] + g[x + 1]) % mod

        total_sum = sum(f.values()) % mod
        return total_sum