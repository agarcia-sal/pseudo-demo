from collections import defaultdict

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        cnt = defaultdict(int)
        d = defaultdict(int)

        for x in nums:
            cnt[x] += 1
            d[x] += 0
            d[x - k] += 1
            d[x + k + 1] -= 1

        ans = 0
        s = 0

        for key in sorted(d.keys()):
            s += d[key]
            possible = min(s, cnt[key] + numOperations)
            if possible > ans:
                ans = possible

        return ans