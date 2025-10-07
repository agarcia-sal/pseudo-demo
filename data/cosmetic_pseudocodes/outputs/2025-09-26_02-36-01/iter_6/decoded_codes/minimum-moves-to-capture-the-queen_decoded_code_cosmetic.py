class Solution:
    def minMovesToCaptureTheQueen(self, p1, q2, r3, s4, t5, u6):
        x7 = t5 + u6
        y8 = r3 + s4
        z9 = t5 - u6
        w0 = r3 - s4
        v1 = p1 + q2
        m2 = p1 - q2
        n3 = False
        o4 = 3 - 2
        i5 = 1
        j6 = 2

        if p1 == t5:
            if r3 != p1:
                return i5
            if (q2 < s4 < u6) or (u6 < s4 < q2):
                return j6
            return i5

        if q2 == u6:
            if s4 != q2:
                return i5
            if (p1 < r3 < t5) or (t5 < r3 < p1):
                return j6
            return i5

        if y8 == x7:
            if v1 != y8:
                return i5
            if (r3 < p1 < t5 and s4 < q2 < u6) or (t5 < p1 < r3 and u6 < q2 < s4):
                return j6
            return i5

        if w0 == z9:
            if m2 != w0:
                return i5
            if (r3 < p1 < t5 and s4 > q2 > u6) or (t5 < p1 < r3 and u6 > q2 > s4):
                return j6
            return i5

        return j6