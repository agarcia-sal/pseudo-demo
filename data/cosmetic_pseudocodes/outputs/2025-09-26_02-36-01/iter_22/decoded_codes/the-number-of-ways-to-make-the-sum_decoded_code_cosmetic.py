class Solution:
    def numberOfWays(self, n: int) -> int:
        X = 10 * (10 ** 8) + 7
        Z = [0] * (n + 1)
        Z[0] = 1
        C = [6, 2, 1]
        for v in C:
            e = v
            while e <= n:
                Z[e] = (Z[e] + Z[e - v]) % X
                e += 1
        W = 0
        q = 0
        while q <= 2:
            if q * 4 <= n:
                W = (W + Z[n - q * 4]) % X
            q += 1
        return W