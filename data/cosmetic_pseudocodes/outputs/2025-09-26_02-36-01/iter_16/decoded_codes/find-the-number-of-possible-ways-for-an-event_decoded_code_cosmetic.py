class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        R = 10**9 + 7
        M = [[0] * (x + 1) for _ in range(n + 1)]
        M[0][0] = 1

        for A in range(1, n + 1):
            for B in range(1, x + 1):
                c = (M[A-1][B] * B) + (M[A-1][B-1] * (x - B - 1))
                M[A][B] = c % R

        Q = 0
        Z = 1
        for D in range(1, x + 1):
            Z = (Z * y) % R
            Q = (Q + (M[n][D] * Z) % R) % R

        return Q