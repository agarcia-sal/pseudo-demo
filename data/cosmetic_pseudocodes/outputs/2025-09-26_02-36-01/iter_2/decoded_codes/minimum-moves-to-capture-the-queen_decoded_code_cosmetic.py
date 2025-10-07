class Solution:
    def minMovesToCaptureTheQueen(self, w, x, y, z, p, q):
        if w == p:
            if y != w:
                return 1
            if (x < z < q) or (q < z < x):
                return 2
            return 1
        if x == q:
            if z != x:
                return 1
            if (w < y < p) or (p < y < w):
                return 2
            return 1
        sum1 = y + z
        sum2 = p + q
        if sum1 == sum2:
            sum3 = w + x
            if sum3 != sum1:
                return 1
            cond1 = (y < w < p and z < x < q)
            cond2 = (p < w < y and q < x < z)
            if cond1 or cond2:
                return 2
            return 1
        diff1 = y - z
        diff2 = p - q
        if diff1 == diff2:
            diff3 = w - x
            if diff3 != diff1:
                return 1
            cond3 = (y < w < p and z > x > q)
            cond4 = (p < w < y and q > x > z)
            if cond3 or cond4:
                return 2
            return 1
        return 2