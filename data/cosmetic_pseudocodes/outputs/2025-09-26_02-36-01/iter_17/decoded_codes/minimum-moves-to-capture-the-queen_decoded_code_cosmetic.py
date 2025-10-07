class Solution:
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f) -> int:
        x1, y1 = a, b
        x2, y2 = c, d
        r1, s1 = e, f

        r2 = x2 + y2
        s2 = r1 + s1

        t1 = x2 - y2
        u1 = r1 - s1

        flagA = False
        flagB = False

        if x1 == r1:
            if x2 != x1:
                return 1
            if (y1 < y2 < s1) or (s1 < y2 < y1):
                return 2
            return 1

        if y1 == s1:
            if r1 != y1:
                return 1
            if (x1 < x2 < r1) or (r1 < x2 < x1):
                return 2
            return 1

        if r2 == s2:
            if (x1 + y1) != r2:
                return 1
            flagA = (x2 < x1 < r1) and (y2 < y1 < s1)
            flagB = (r1 < x1 < x2) and (s1 < y1 < y2)
            if flagA or flagB:
                return 2
            return 1

        if t1 == u1:
            if (x1 - y1) != t1:
                return 1
            flagA = (x2 < x1 < r1) and (y2 > y1 > s1)
            flagB = (r1 < x1 < x2) and (s1 > y1 > y2)
            if flagA or flagB:
                return 2
            return 1

        return 2