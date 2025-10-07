class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        def swapIfGreater(x, y):
            return (y, x) if x > y else (x, y)

        if a == e:
            if c != a:
                return 1
            p23q4w5, l9m8n7 = swapIfGreater(b, f)
            v0b1c2 = d
            if (p23q4w5 < v0b1c2 < l9m8n7) or (l9m8n7 < v0b1c2 < p23q4w5):
                return 2
            return 1

        if b == f:
            if d != b:
                return 1
            r4t5y6, j7k8l9 = swapIfGreater(a, e)
            u3i2o1 = c
            if (r4t5y6 < u3i2o1 < j7k8l9) or (j7k8l9 < u3i2o1 < r4t5y6):
                return 2
            return 1

        s24r5t6 = c + d
        y87u65 = e + f
        if s24r5t6 == y87u65:
            if (a + b) != s24r5t6:
                return 1
            r4t5y6, j7k8l9 = swapIfGreater(c, e)
            p23q4w5, l9m8n7 = swapIfGreater(d, b)
            cond1 = r4t5y6 < a < j7k8l9 and p23q4w5 < l9m8n7 < f
            cond2 = j7k8l9 < a < r4t5y6 and f < l9m8n7 < p23q4w5
            if cond1 or cond2:
                return 2
            return 1

        c2 = c - d
        e2 = e - f
        if c2 == e2:
            if (a - b) != c2:
                return 1
            r4t5y6, j7k8l9 = swapIfGreater(c, e)
            p23q4w5, l9m8n7 = swapIfGreater(b, f)
            # Fixed variable names from pseudocode
            cond1 = r4t5y6 < a < j7k8l9 and p23q4w5 > l9m8n7 > f
            cond2 = j7k8l9 < a < r4t5y6 and l9m8n7 > f > p23q4w5
            if cond1 or cond2:
                return 2
            return 1

        return 2