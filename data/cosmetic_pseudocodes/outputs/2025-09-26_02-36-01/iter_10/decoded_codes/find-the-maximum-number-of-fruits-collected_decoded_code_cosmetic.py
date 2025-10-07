from math import inf

class Solution:
    def maxCollectedFruits(self, fruits):
        p = len(fruits)
        m1 = [(1, 1), (1, 0)]
        m2 = [(1, 0), (1, -1), (1, 1)]
        m3 = [(-1, 1), (0, 1), (1, 1)]
        cache = {}

        def compute(a, b, c, d, e, f):
            # Out of bounds check
            if not (0 <= a < p and 0 <= b < p and 0 <= c < p and 0 <= d < p and 0 <= e < p and 0 <= f < p):
                return -inf

            # Terminal condition: all positions at bottom-right corner
            if a == b == c == d == e == f == p - 1:
                return fruits[p - 1][p - 1]

            key = (a, b, c, d, e, f)
            if key in cache:
                return cache[key]

            sumValue = fruits[b][a]

            if (a == c and b == d) or (a == e and b == f):
                sumValue = 0

            if (c == e) and (d == f):
                sumValue += fruits[d][c]
            else:
                sumValue += fruits[d][c] + fruits[f][e]

            best = -inf

            for dx1, dy1 in m1:
                for dx2, dy2 in m2:
                    for dx3, dy3 in m3:
                        val = compute(a + dx1, b + dy1, c + dx2, d + dy2, e + dx3, f + dy3)
                        if val > best:
                            best = val

            cache[key] = sumValue + best
            return sumValue + best

        return compute(0, 0, 0, p - 1, p - 1, 0)