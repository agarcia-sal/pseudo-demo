class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        bar = 1_000_000_000 + 7
        alpha = [[0] * (x + 1) for _ in range(n + 1)]
        alpha[0][0] = 1

        for u in range(1, n + 1):
            for v in range(1, x + 1):
                w = ((alpha[u - 1][v] * v) + (alpha[u - 1][v - 1] * (x - v - 1))) % bar
                alpha[u][v] = w

        omega = 0
        gamma = 1
        for q in range(1, x + 1):
            gamma = (gamma * y) % bar
            omega = (omega + (alpha[n][q] * gamma)) % bar

        return omega