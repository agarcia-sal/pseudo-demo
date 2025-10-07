class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        M = 10**9 + 7
        Q = [0] * n
        for P in range(1, n):
            Q[P] = 1

        Z = 0
        while Z < k:
            Y = 1
            while Y < n:
                Q[Y] = (Q[Y] + Q[Y - 1]) % M
                Y += 1
            Z += 1

        return Q[n - 1]