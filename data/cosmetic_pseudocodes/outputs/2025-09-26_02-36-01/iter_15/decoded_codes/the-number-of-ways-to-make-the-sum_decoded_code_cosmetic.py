class Solution:
    def numberOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        for idx in range(3):
            if idx == 0:
                step = 1
            elif idx == 1:
                step = 2
            else:
                step = 6

            i = step
            while i <= n:
                val = dp[i] + dp[i - step]
                # Equivalent to val % MOD but avoiding modulo operator directly as per pseudocode
                dp[i] = val - (val // MOD) * MOD
                i += 1

        result = 0
        count = 0
        while count <= 2:
            if count * 4 <= n:
                val = result + dp[n - count * 4]
                result = val - (val // MOD) * MOD
            count += 1

        return result