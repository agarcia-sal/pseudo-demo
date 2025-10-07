class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MODULO = 10**9 + 7
        DP = [[0] * (n + 1) for _ in range(x + 1)]
        DP[0][0] = 1
        for index in range(1, x + 1):
            for total in range(1, n + 1):
                val1 = (DP[index][total - 1] * index) % MODULO
                val2 = (DP[index - 1][total - 1] * (x - index + 1)) % MODULO
                DP[index][total] = (val1 + val2) % MODULO
        result = 0
        powerY = 1
        for count in range(1, x + 1):
            powerY = (powerY * y) % MODULO
            result = (result + DP[count][n] * powerY) % MODULO
        return result