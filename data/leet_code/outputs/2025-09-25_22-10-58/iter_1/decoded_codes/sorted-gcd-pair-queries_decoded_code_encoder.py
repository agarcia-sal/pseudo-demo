from collections import Counter
from itertools import accumulate
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums, queries):
        mx = max(nums)
        cnt = Counter(nums)
        cnt_g = [0] * (mx + 1)

        for i in range(mx, 0, -1):
            v = 0
            j = i
            while j <= mx:
                c = cnt[j]
                v += c
                cnt_g[i] -= cnt_g[j]
                j += i
            cnt_g[i] += v * (v - 1) // 2

        s = list(accumulate(cnt_g))
        result = []
        for q in queries:
            pos = bisect_right(s, q)
            result.append(pos)
        return result