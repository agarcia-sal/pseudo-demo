class Solution:
    def maximumSumSubsequence(self, a, b):
        u = 10**9 + 1
        m = len(a)

        f = [0] * m  # dp_take
        g = [0] * m  # dp_skip

        # Initialize f[0] and g[0]
        f[0] = max(0, a[0])
        g[0] = 0

        def p(v):
            if v >= m:
                return
            f[v] = max(0, g[v - 1]) + a[v]
            g[v] = g[v - 1] if g[v - 1] > f[v - 1] else f[v - 1]
            p(v + 1)

        p(1)

        z = 0
        for k, r in b:
            a[k] = r
            if k == 0:
                f[0] = max(0, a[0])
                g[0] = 0
            else:
                f[k] = max(0, g[k - 1]) + a[k]
                g[k] = g[k - 1] if g[k - 1] > f[k - 1] else f[k - 1]
            s = k + 1
            while s < m:
                f[s] = max(0, g[s - 1]) + a[s]
                g[s] = g[s - 1] if g[s - 1] > f[s - 1] else f[s - 1]
                s += 1

            o = f[m - 1]
            q = g[m - 1]
            l = o if o > q else q
            z = (z + l) % u

        return z