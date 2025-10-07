class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if a == e:
            if c != a:
                return 1
            if (b < d < f) or (f < d < b):
                return 2
            return 1

        if b == f:
            if d != b:
                return 1
            if (a < c < e) or (e < c < a):
                return 2
            return 1

        if c + d == e + f:
            if a + b != c + d:
                return 1
            if (c < a < e and d < b < f) or (e < a < c and f < b < d):
                return 2
            return 1

        if c - d == e - f:
            if a - b != c - d:
                return 1
            if (c < a < e and d > b > f) or (e < a < c and f > b > d):
                return 2
            return 1

        return 2