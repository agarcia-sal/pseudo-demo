class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        Q = 10**9 + 7
        U = [1] * n

        def R(X):
            for j in range(1, len(X)):
                X[j] = (X[j] + X[j - 1]) % Q

        z = 0
        while z < k:
            R(U)
            z += 1

        return U[n - 1]