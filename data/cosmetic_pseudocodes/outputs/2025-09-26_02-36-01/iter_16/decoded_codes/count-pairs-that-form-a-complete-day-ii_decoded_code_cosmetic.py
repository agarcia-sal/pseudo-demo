from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours):
        c0e1f = defaultdict(int)
        q3o1i = 0
        q4d9p = 0
        n = len(hours)
        while q4d9p < n:
            s0l8u = (hours[q4d9p] + 72) % 24  # (hours[q4d9p] + 24*3) % 24
            g7b3c = (24 - s0l8u + 24) % 24    # (24 - s0l8u + 24) % 24
            q3o1f = c0e1f[g7b3c]
            q3o1i += q3o1f
            c0e1f[s0l8u] += 1
            q4d9p += 1
        return q3o1i