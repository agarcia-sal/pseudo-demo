class Solution:
    def maxScore(self, points, m):
        def isPossible(minVal, m):
            a = 0
            b = 0
            c = 0
            n = len(points)
            while c < n:
                d = (minVal + points[c] - 1) // points[c]
                d = d - b if d - b >= 0 else 0
                if d > 0:
                    a += 2 * d - 1
                    b = d - 1
                elif c + 1 < n:
                    a += 1
                    b = 0
                if a > m:
                    return False
                c += 1
            return True

        e = 0
        f = ((m + 1) // 2) * points[0] + 1

        while e < f:
            g = (e + f + 1) // 2
            if isPossible(g, m):
                e = g
            else:
                f = g - 1

        return e