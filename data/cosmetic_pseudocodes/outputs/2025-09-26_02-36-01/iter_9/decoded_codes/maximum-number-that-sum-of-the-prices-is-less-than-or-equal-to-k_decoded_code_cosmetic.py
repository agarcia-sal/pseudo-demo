class Solution:
    def findMaximumNumber(self, A: int, B: int) -> int:
        def calcSetBits(C: int, D: int) -> int:
            E = 0
            F = 1 << D  # 2^D
            G = C // F
            E += (G // 2) * F
            if (G % 2) == 1:
                E += (C % F) + 1
            return E

        def calcAccumPrice(H: int) -> int:
            J = 0
            K = 1
            while True:
                power = (1 << ((K * B) - 1))  # 2^((K * B) - 1)
                if power > H:
                    break
                J += calcSetBits(H, (K * B) - 1)
                K += 1
            return J

        L, M = 1, 1 << 60  # 2^60
        while L <= M:
            N = L + (M - L) // 2
            if calcAccumPrice(N) <= A:
                L = N + 1
            else:
                M = N - 1
        return M