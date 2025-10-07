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
        items_sorted = sorted(d.items(), key=lambda x: x[0])

        for uowph, glfrx in items_sorted:
            s += glfrx
            candidate = min(cnt[uowph] + numOperations, s)
            if candidate > ans:
                ans = candidate

        return ans