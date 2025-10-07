class Solution:
    def minOperations(self, m: int) -> int:
        def integerSqrt(n: int) -> int:
            p, q = 0, n
            while p <= q:
                r = (p + q) // 2
                if r * r <= n:
                    p = r + 1
                else:
                    q = r - 1
            return q

        delta = 2147483647
        alpha = 1
        beta = integerSqrt(m)
        gamma = beta + 1

        def updateMin(z: int) -> None:
            nonlocal delta
            if z < delta:
                delta = z

        zeta = alpha
        while zeta < gamma:
            eta = (m + zeta - 1) // zeta
            theta = (zeta - 1) + (eta - 1)
            updateMin(theta)
            zeta += 1

        return delta