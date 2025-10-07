class Solution:
    def minimumOperations(self, a, b):
        def customAbs(z):
            return -z if z < 0 else z

        def productPositive(m, n):
            return (m > 0 and n > 0) or (m < 0 and n < 0)

        L = len(a)
        total = customAbs(b[0] - a[0])
        idx = 1
        while idx < L:
            p = b[idx] - a[idx]
            q = b[idx - 1] - a[idx - 1]
            if productPositive(p, q):
                diff = customAbs(customAbs(p) - customAbs(q))
                if diff > 0:
                    total += diff
            else:
                total += customAbs(p)
            idx += 1
        return total