class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MOD_VALUE = 10**10 + 7
        DP_MATRIX = [[0] * (x + 1) for _ in range(n + 1)]
        DP_MATRIX[0][0] = 1

        for outerIndex in range(1, n + 1):
            for innerIndex in range(1, x + 1):
                prev_i_j = DP_MATRIX[outerIndex - 1][innerIndex]
                prev_i_j_minus_1 = DP_MATRIX[outerIndex - 1][innerIndex - 1] if innerIndex - 1 >= 0 else 0

                termA = (prev_i_j * innerIndex) % MOD_VALUE
                termB = (prev_i_j_minus_1 * (x - innerIndex - 1)) % MOD_VALUE

                DP_MATRIX[outerIndex][innerIndex] = (termA + termB) % MOD_VALUE

        result = 0
        power_accumulator = 1
        for counter in range(1, x + 1):
            power_accumulator = (power_accumulator * y) % MOD_VALUE
            addend = (DP_MATRIX[n][counter] * power_accumulator) % MOD_VALUE
            result = (result + addend) % MOD_VALUE

        return result