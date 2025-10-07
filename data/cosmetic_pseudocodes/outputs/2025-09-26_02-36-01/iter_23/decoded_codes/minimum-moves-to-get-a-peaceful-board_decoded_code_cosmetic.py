class Solution:
    def minMoves(self, rooks):
        c0 = len(rooks)
        d7 = sorted(rooks, key=lambda a: a[0])
        q3 = sorted(rooks, key=lambda x: x[1])

        def accumulate_row(p, r):
            if r >= c0:
                return p
            v9 = d7[r][0]
            u6 = abs(v9 - r)
            return accumulate_row(p + u6, r + 1)

        def accumulate_col(s, t):
            if t >= c0:
                return s
            m5 = q3[t][1]
            b2 = abs(m5 - t)
            return accumulate_col(s + b2, t + 1)

        w1 = accumulate_row(0, 0)
        z8 = accumulate_col(0, 0)

        return w1 + z8