class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MODULO_VALUE = 10**9 + 7

        def MulMod(a: int, b: int) -> int:
            result = 0
            base = a % MODULO_VALUE
            multiplier = b % MODULO_VALUE
            while multiplier > 0:
                if multiplier & 1 != 0:
                    result = (result + base) % MODULO_VALUE
                base = (base + base) % MODULO_VALUE
                multiplier >>= 1
            return result

        matrix = [[0] * (x + 1) for _ in range(n + 1)]
        matrix[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, x + 1):
                term1 = MulMod(matrix[i - 1][j], j)
                term2 = MulMod(matrix[i - 1][j - 1], x - (j - 1))
                matrix[i][j] = (term1 + term2) % MODULO_VALUE

        result_value = 0
        power_accumulator = 1
        for j in range(1, x + 1):
            power_accumulator = (power_accumulator * y) % MODULO_VALUE
            increment_value = MulMod(matrix[n][j], power_accumulator)
            result_value = (result_value + increment_value) % MODULO_VALUE

        return result_value